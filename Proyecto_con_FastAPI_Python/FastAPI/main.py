from database import Base, engine
from models import Producto, Trabajador

Base.metadata.create_all(bind=engine)

from fastapi import FastAPI, Depends, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Producto
import pdfkit
from fastapi.responses import StreamingResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
def mostrar_inicio(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/leer_inventario", response_class=HTMLResponse)
def leer_inventario(request: Request, db: Session = Depends(get_db)):
    productos = db.query(Producto).all()     
    return templates.TemplateResponse("inventario.html", {"request": request, "productos": productos})

@app.post("/agregar", response_class=HTMLResponse)
def agregar_producto(request: Request, nombre: str = Form(...), cantidad: int = Form(...), precio: int = Form(...), unidad_medida: str = Form(...), trabajador_nombre: str = Form(...), db: Session = Depends(get_db)):
    trabajador = db.query(Trabajador).filter(Trabajador.nombre == trabajador_nombre).first()
    if not trabajador:
        trabajador = Trabajador(nombre=trabajador_nombre)
        db.add(trabajador)
        db.commit()
        db.refresh(trabajador)
    producto = Producto(nombre=nombre, cantidad=cantidad, precio=precio, unidad_medida=unidad_medida, trabajador_id=trabajador.id)
    db.add(producto)
    db.commit()
    db.refresh(producto)
    productos = db.query(Producto).all()
    return templates.TemplateResponse("inventario.html", {
        "request": request,
        "productos": productos,
        "mensaje": "Producto creado correctamente"
    })


from fastapi import Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

@app.get("/listado", response_class=HTMLResponse)
def mostrar_listado(request: Request, db: Session = Depends(get_db)):
    mensaje = request.query_params.get("mensaje")
    productos = db.query(Producto).all()
    return templates.TemplateResponse("inventario_listado.html", {"request": request, "productos": productos, "mensaje": mensaje})

#solicitud de eliminar producto
from fastapi.responses import RedirectResponse

@app.post("/eliminar/{producto_id}")
def eliminar_producto(producto_id: int, db: Session = Depends(get_db)):
    producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if producto:
        db.delete(producto)
        db.commit()
    return RedirectResponse(url="/listado?mensaje=eliminado", status_code=303)

from fastapi import Form

@app.get("/editar/{producto_id}", response_class=HTMLResponse)
def editar_producto_form(request: Request, producto_id: int, db: Session = Depends(get_db)):
    producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if not producto:
        return templates.TemplateResponse("inventario_listado.html", {
            "request": request,
            "productos": db.query(Producto).all(),
            "mensaje": "Producto no encontrado"
        })
    return templates.TemplateResponse("editar.html", {"request": request, "producto": producto})

@app.post("/editar/{producto_id}", response_class=HTMLResponse)
def editar_producto(request: Request, producto_id: int, nombre: str = Form(...), cantidad: int = Form(...), precio: int = Form(...), unidad_medida: str = Form(...), trabajador_nombre: str = Form(...), db: Session = Depends(get_db)):
    producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if producto:
        trabajador = db.query(Trabajador).filter(Trabajador.nombre == trabajador_nombre).first()
        if not trabajador:
            trabajador = Trabajador(nombre=trabajador_nombre)
            db.add(trabajador)
            db.commit()
            db.refresh(trabajador)
        producto.nombre = nombre
        producto.cantidad = cantidad
        producto.precio = precio
        producto.unidad_medida = unidad_medida
        producto.trabajador_id = trabajador.id
        db.commit()
        mensaje = "Producto actualizado correctamente"
    else:
        mensaje = "Producto no encontrado"
    productos = db.query(Producto).all()
    return templates.TemplateResponse("inventario_listado.html", {
        "request": request,
        "productos": productos,
        "mensaje": mensaje
    })


@app.get("/descargar_pdf")
def descargar_pdf(db: Session = Depends(get_db)):
    productos = db.query(Producto).all()
    from fastapi.templating import Jinja2Templates
    from starlette.requests import Request as StarletteRequest
    templates = Jinja2Templates(directory="templates")
    fake_request = StarletteRequest(scope={"type": "http"})
    html_content = templates.get_template("inventario_listado.html").render({"request": fake_request, "productos": productos, "mensaje": ""})
    options = {
        "enable-local-file-access": ""
    }
    pdf = pdfkit.from_string(html_content, False, options=options)
    return StreamingResponse(
        iter([pdf]),
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=Inventario.pdf"}
    )
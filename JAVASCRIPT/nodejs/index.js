(async () => {
    const chalk = await import('chalk');
    
    console.log(chalk.default.blue('Hello blue world!'));
    console.log(chalk.default.red('Hello red world!'));
})();
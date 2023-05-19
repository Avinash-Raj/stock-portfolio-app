## Stock Portfolio App

This is a simple PyQt6/PySide6 application that allows users to keep track of the stocks they own and their performance.



https://github.com/Avinash-Raj/stock-portfolio-app/assets/3929632/e313d2e7-f9c2-4b08-ab66-60fd6211b603





#### Features
---

- Add new stocks to your portfolio
- Edit the details of existing stocks
- Delete stocks that you no longer own
- View your portfolio's current value and gain/loss

#### Installation
---

Clone the repository: 

    git clone https://github.com/Avinash-Raj/stock-portfolio-app.git

Use `python version >= 3.11`

Install the required dependencies: 

    poetry install

#### Build and Run
---

Create a virtual environment using python version `>=3.11` and then activate it. 
Get into the project root directory and then run the below commands for installing mystocks app locally.

    $ poetry build

Above command creates a dist directory on the project's root folder along with the `mystocks.tar.gz` package. Now do a pip install.

    $ pip install ./dist/mystocks-0.1.0.tar.gz

Now it's the time to run the app.

    $ run_migrations
    $ mystocks

#### Contributing
---

Contributions are always welcome! If you would like to contribute to the project, please submit a pull request.

#### License
---

This project is licensed under the MIT License. See the LICENSE file for details.

#### Credits
---

The following third-party libraries were used in this project:

    PySide6
    yfinance
    sqlite3
    currencyconverter

You can customize this README.md file by replacing the relevant information with your own project details. You might also want to include information about the features you plan to implement in the future, any known issues or limitations, and instructions for running tests or contributing to the project.

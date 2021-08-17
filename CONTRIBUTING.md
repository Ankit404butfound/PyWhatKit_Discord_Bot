# Guidelines for Contributing and Raising Issues

## Thanks for considering contributing to this Project!🥳

## **Raising Issues:** ✋

- _If you want to ask anything about this project, please feel free to open an issue [here](https://github.com/Ankit404butfound/PyWhatKit_Discord_Bot/issues)._
- _Any bugs that are found in the documentation or in any part of bot, can be reported using the Bug Report Template._
- _Do not upload any compiled binaries with your PR._ ❌
- _Please be polite and helpful to everyone._ 🙂

---

## **Contributing:** 📝

### _If you would like to provide a fix for a problem you can do so by opening a Pull Request [here](https://github.com/Ankit404butfound/PyWhatKit_Discord_Bot/pulls). Below are some points to consider:_

<br>

- _Please open a Draft PR if you want to change a lot of things._
- _Provide a list of all the fixes that you have done in the PR description._
- _If your PR fixes an Issue, consider mentioning it with `fixes #IssueNumber`._
- _Provide all the details in the PR template as applicable._
- _If you want to add a new feature please open an issue first to discuss it or your changes may not get merged._

---

## Code Formatting

_Please make sure that your code follows the [PEP8](https://www.python.org/dev/peps/pep-0008/) guidelines._

_Before committing your changes to the repository, run `pre-commit run --all-files` or `pipenv run lint` this will highlight and fix some errors._

_For PyCharm users you can use the key combination `Ctrl + Alt + L` to format your code._

_For VsCode users, create a `.vscode` folder in your project root and create a `settings.json` file inside it. Place the following in the `settings.json` file:_

```json
{
  "editor.formatOnSave": true,
  "python.formatting.provider": "autopep8"
}
```

_You can also use `autopep8` directly from the command line using `autopep8 -i filename`._
_After fixing all the errors, push your changes and then open a PR._

## **Setting up the Environment:** 💻

### _Please ensure that you have Python version 3.9._

### _This guides you through the setting up the Environment for working with the project._

<br>

1. _Fork the repository._
2. _Clone it to your local machine to work with the Project._
3. _Install pipenv if you haven't using `pip3 install pipenv`._
4. _Create a Virtual Environment with pipenv using `pipenv shell`._
5. _Install the project dependencies using `pipenv install --dev`._
6. _Open the Project in the Editor of your choice._
7. _Congratulations, you are now ready to Contribute._ 🎉

> NOTE: For linux users, you will need to install `psycopg2-binary` instead of `psycopg2` in the step 5.

## **Setting Up the Bot** 🤖️

### _Follow the steps below to set up the Bot:_

1. _Follow this guide [here](https://realpython.com/how-to-make-a-discord-bot-python/) on how to create a server and the Bot._
2. _After getting all the required values, create a `.env` file in the project root using the `.env.example` as a template and place the values in it._
3. _Now, if you run the `__main__.py` file you should see the BOT online in your test server._

> NOTE: It is optional for you to set up the PostgreSQL database.

### _If you need any other help regarding CONTRIBUTING to the Bot, please join our discord server [here](https://discord.gg/PvfFgYpDuK)._

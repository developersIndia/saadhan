# saadhan

Saadhan is a resource hub for the [r/developersIndia](https://reddit.com/r/developersIndia) community

[![Discord](https://img.shields.io/discord/669880381649977354?color=%237289da&label=Discord&logo=Discord)](https://discordapp.com/invite/MKXMSNC)
[![Subreddit subscribers](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fdevelopersindia.github.io%2Fmetrics%2Fdata%2F&query=%24.totalMembers&suffix=%20members&style=flat&logo=reddit&label=r%2FdevelopersIndia&color=orange&link=https%3A%2F%2Fwww.reddit.com%2Fr%2FdevelopersIndia
)](https://www.reddit.com/r/developersIndia/)
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg)](#contributors-)


> [!IMPORTANT]  
> We are currently migrating our hosting provider. During this time, the `saadhan.developersindia.in` link will be unavailable. In the meantime, please use this temporary URL: https://saadhan-hplc.onrender.com/

## ❓ What is this
- Saadhan is an app to aggregate and provide tech resources to learn from.
- Resources are contributed by community. [Contribute your favourite resources](https://github.com/developersIndia/resources)
- The website is built using Flask as backend and [HTMX](https://htmx.org/) with [Bulma](https://bulma.io) as frontend.

## 🧰 Installation
### Using Virtual environment 🎥

1. Initialise a virtual environment.

   ```bash
   cd saadhan
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```
3. Run development server.
   ```bash
   make run
   ```

### Using Docker 🐬

1. Build docker image
   ```make
   make build-docker
   ```
2. Run image
   ```make
   make docker
   ```

# 📜 License

This project is licensed under the GPL-3.0 License. See the [LICENSE](LICENSE) file for details.

# 👋 Contributing

Please read the [CONTRIBUTING](CONTRIBUTING.md) guidelines for the process of submitting pull requests to us.

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/the-sinner"><img src="https://avatars.githubusercontent.com/u/34604329?v=4?s=100" width="100px;" alt="Shalabh Agarwal"/><br /><sub><b>Shalabh Agarwal</b></sub></a><br /><a href="https://github.com/developersIndia/saadhan/commits?author=the-sinner" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/HarshRaj2717"><img src="https://avatars.githubusercontent.com/u/90465144?v=4?s=100" width="100px;" alt="Harsh Raj"/><br /><sub><b>Harsh Raj</b></sub></a><br /><a href="https://github.com/developersIndia/saadhan/commits?author=HarshRaj2717" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/rashhocket"><img src="https://avatars.githubusercontent.com/u/124589872?v=4?s=100" width="100px;" alt="rashhocket"/><br /><sub><b>rashhocket</b></sub></a><br /><a href="https://github.com/developersIndia/saadhan/commits?author=rashhocket" title="Code">💻</a> <a href="https://github.com/developersIndia/saadhan/issues?q=author%3Arashhocket" title="Bug reports">🐛</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://sid4stuff.tech/"><img src="https://avatars.githubusercontent.com/u/78897025?v=4?s=100" width="100px;" alt="K Hari Aneesh Siddhartha"/><br /><sub><b>K Hari Aneesh Siddhartha</b></sub></a><br /><a href="https://github.com/developersIndia/saadhan/commits?author=ansid0102" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://nvchad.com"><img src="https://avatars.githubusercontent.com/u/59060246?v=4?s=100" width="100px;" alt="Sidhanth Rathod"/><br /><sub><b>Sidhanth Rathod</b></sub></a><br /><a href="https://github.com/developersIndia/saadhan/issues?q=author%3Asiduck" title="Bug reports">🐛</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/MohitBansal321"><img src="https://avatars.githubusercontent.com/u/78220157?v=4?s=100" width="100px;" alt="Mohit Bansal"/><br /><sub><b>Mohit Bansal</b></sub></a><br /><a href="https://github.com/developersIndia/saadhan/commits?author=MohitBansal321" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/mustafa-kapadia1483"><img src="https://avatars.githubusercontent.com/u/60058032?v=4?s=100" width="100px;" alt="Mustafa Kapadia"/><br /><sub><b>Mustafa Kapadia</b></sub></a><br /><a href="https://github.com/developersIndia/saadhan/commits?author=mustafa-kapadia1483" title="Code">💻</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/darshil-here"><img src="https://avatars.githubusercontent.com/u/104206815?v=4?s=100" width="100px;" alt="Darshil Prajapati"/><br /><sub><b>Darshil Prajapati</b></sub></a><br /><a href="https://github.com/developersIndia/saadhan/commits?author=darshil-here" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/heppymxm"><img src="https://avatars.githubusercontent.com/u/130273246?v=4?s=100" width="100px;" alt="Kartik Kumar"/><br /><sub><b>Kartik Kumar</b></sub></a><br /><a href="https://github.com/developersIndia/saadhan/commits?author=heppymxm" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://haspper.neocities.org/"><img src="https://avatars.githubusercontent.com/u/121102787?v=4?s=100" width="100px;" alt="yump"/><br /><sub><b>yump</b></sub></a><br /><a href="https://github.com/developersIndia/saadhan/commits?author=yumpyy" title="Code">💻</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!

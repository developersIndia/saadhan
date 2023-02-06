# saadhan

Saadhan is a resource hub for the [r/developersIndia](https://reddit.com/r/developersIndia) community

[![Discord](https://img.shields.io/discord/669880381649977354?color=%237289da&label=Discord&logo=Discord)](https://discordapp.com/invite/MKXMSNC)
[![Subreddit subscribers](https://img.shields.io/reddit/subreddit-subscribers/developersIndia?style=social)](https://www.reddit.com/r/developersIndia/)
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg)](#contributors-)

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
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!

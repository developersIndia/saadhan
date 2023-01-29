# saadhan

Saadhan is a resource hub for the [r/devleopersIndia](https://reddit.com/r/developersIndia) community

[![Discord](https://img.shields.io/discord/669880381649977354?color=%237289da&label=Discord&logo=Discord)](https://discordapp.com/invite/MKXMSNC)
[![Subreddit subscribers](https://img.shields.io/reddit/subreddit-subscribers/developersIndia?style=social)](https://www.reddit.com/r/developersIndia/)


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


[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
  <h3 align="center">Weekly event report telegram bot</h3>

  <p align="center">
    This is a telegram bot you can use to make a report of the weeks events and send it as message to a telegram channel, group or user. 
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project can be used to make reports like seen in the following image:
![Product Name Screen Shot][product-screenshot]


### Built With

* [Python](https://www.python.org/)
* [Telegram Bot API](https://core.telegram.org/bots/api)
* [Requests: HTTPS for Humans](https://requests.readthedocs.io/en/master/)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* Python [https://www.python.org/](https://www.python.org/)
* Python Requests
  ```sh
  python -m pip install requests
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/prestitre/weekly-event-telegram-bot.git
   ```
2. Configure your bot by adding your token, calendar(ics-link), time_difference(your time difference from your calendar source) and message_reciepient(user id). To know more of the Telegram Bot API checkout: [https://core.telegram.org/bots/api](https://core.telegram.org/bots/api). And how to get user id checkout: [stackoverflow](https://stackoverflow.com/questions/32683992/find-out-my-own-user-id-for-sending-a-message-with-telegram-api) and for groups id: [stackoverflow](https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id)

3. Edit the weekly report in server.py in the way you want it look. Checkout markdown formatting from: [https://core.telegram.org/bots/api#formatting-options](https://core.telegram.org/bots/api#formatting-options)

4. Run the program inside telegram-bot folder with the following command
   ```sh
   python server.py
   ```




<!-- USAGE EXAMPLES -->
## Usage

This bot was created to be easily used with cronjob to use it automatically on weekly bases.

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Paavo Keski-Orvola - [@ThePrestitre](https://twitter.com/ThePrestitre) - paavo.keskiorvola@gmail.com

Project Link: [https://github.com/prestitre/weekly-event-telegram-bot](https://github.com/prestitre/weekly-event-telegram-bot)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [Luuppi ry](www.luuppi.fi)
* [Telegram Bot API](https://core.telegram.org/api)
* [Requests](https://requests.readthedocs.io/en/master/)
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)






<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/prestitre/repo.svg?style=for-the-badge
[contributors-url]: https://github.com/prestitre/weekly-event-telegram-bot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/prestitre/repo.svg?style=for-the-badge
[forks-url]: https://github.com/prestitre/weekly-event-telegram-bot/network/members
[stars-shield]: https://img.shields.io/github/stars/prestitre/repo.svg?style=for-the-badge
[stars-url]: https://github.com/prestitre/weekly-event-telegram-bot/stargazers
[issues-shield]: https://img.shields.io/github/issues/prestitre/repo.svg?style=for-the-badge
[issues-url]: https://github.com/prestitre/weekly-event-telegram-bot/issues
[license-shield]: https://img.shields.io/github/license/prestitre/repo.svg?style=for-the-badge
[license-url]: https://github.com/prestitre/weekly-event-telegram-bot/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/paavo-keski-orvola-b65161142/
[product-screenshot]: images/screenshot.png
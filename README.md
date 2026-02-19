#  PMP - Python Music Player

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/PyQt6-v6.4+-41CD52?style=for-the-badge&logo=qt&logoColor=white" alt="PyQt6">
  <img src="https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg" alt="CCBYNCSA">
</p>

---

##  Project Overview
**PMP (Python Music Player)** is a desktop audio application designed for users who value a clean, modular, and customizable listening experience. Built with **Python** and **PyQt6**, it focuses on modern UI/UX principles, featuring a scalable architecture and a fully customizable design via QSS.

---

##  Planned Functionalities

The project is actively developing the following core modules and features:

###  Music Management
* **Personal Library:** A centralized hub for all your local audio files.
* **Custom Playlists:** Create, edit, and organize your favorite tracks.
* **Smart History:** Quick access to your **Recently Played** tracks.
* **Favorites:** One-click "Like" system to bookmark your top hits.
* **Categorization:** Browse your collection by **Artist** or **Album** with ease.

###  "Get Music" Integration
A dedicated section designed to expand your library directly from the app:
* **Digital Stores:** Planned integration with popular platforms like **iStore** and **Google Play**.
* **YouTube Downloader:** Built-in tool to convert and download audio directly from YouTube for offline listening.

---

##  Tech Stack
* **Core:** Python 3.10+
* **GUI Framework:** PyQt6
* **Styling:** Custom QSS (Qt Style Sheets).
* **Typography:** Integrated **Lato** font family for superior readability.
* **Architecture:** Fully modular component-based structure (`TopBar`, `Sidebar`, `Workspace`).

---

##  Project Structure
```text
PMP_PythonMusicPlayer/
├── mainApplication.py    # Main entry point
├── GUI/                  # Modular UI Components
│   ├── __init__.py       
│   ├── sidebar.py        # Navigation & Filters
│   ├── topNavigation.py  # Global controls
|   ├── style.qss         # Global Qss styling
│   └── workspace.py      # Content & Player view
└── assets/               # Branding, Fonts & Icons

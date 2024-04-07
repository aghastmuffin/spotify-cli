from setuptools import setup

# Fabricated long description
long_description = """
spotify-win-cli is a command-line tool that allows users to interact with Spotify's API seamlessly. With spotify-win-cli, users can perform a variety of tasks, including searching for tracks, albums, and artists, creating and managing playlists, and even controlling playback directly from the terminal.

Key Features:
- Search: Easily search for tracks, albums, and artists using simple commands.
- Playlist Management: Create, delete, and manage your Spotify playlists effortlessly.
- Playback Control: Control playback of your favorite tracks without leaving the terminal.
- Integration: Seamlessly integrates with your existing Spotify account, providing access to all your playlists and saved tracks.

Installation:
You can install spotify-win-cli via pip:
"""
# Delegate all other configuration to pyproject.toml

setup(
    name="spotify-win-cli",
    version="3.0.0",
    long_description=long_description,
    long_description_content_type="text/plain",  # Adjust if using a different markup format
)

# EOX v3.3

- Fixed [unability to show collections correctly](https://github.com/ygz213/EasyOpenX/issues/15)
- Added ability to check given file/folder paths when creating or editing collection
- Started to use ttkbootstrap
- Changes on code

# EOX v3.0

- Fixed issues about app works for only latest collections ([#12](https://github.com/ygz213/EasyOpenX/issues/12)) ([#13](https://github.com/ygz213/EasyOpenX/issues/13))
- Changes on code

# EOX v2.3

- Made windows not resizable
- Edit collection window will destroy itself when it lose focus (to prevent the problem that it does not get closed after new window opened)
- Windows will get focus when opening
- Windows will not leave from foreground (except edit collection window)

# EOX v2.2

- Fixed the [issue that does not let apps get opened simultaneously](https://github.com/ygz213/EasyOpenX/issues/8)
- Added ability to delete collections
- Added ability to edit collections

# EOX v2.1

- Fixed [unability to open app on Linux or MacOS #2](https://github.com/ygz213/EasyOpenX/issues/6)
- Added ability to delete `__pycache__` on exit

# EOX v2.0

- Added ability to create collections
- Added ability to show existing collections
- Added ability to run collections

## BETA - EOX v1.5

- Added icon
- Made UI look better
- Deleted app-based UI since this is a collection-opening app
- Seperated handler class

# EOX v1.1

- Fixed [unability to open app on Linux](https://github.com/ygz213/EasyOpenX/issues/3) or MacOS
- Changed initial directory and title of app selector and deleted .EXE file type
- Changes on code

# EOX v1.0

- Fixed [invisible buttons](https://github.com/Ernesto905/EasyOpen/issues/1) (upstream issue)
- `fileHandler.py` moved to `main.py`

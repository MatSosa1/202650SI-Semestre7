import shutil
from pathlib import Path

PATH_PROJECT = 'Proyecto/'
PATH_OLD_PROJECT = 'Proyecto_old/'

KEEP_RUNNING = True

# Copy the data from one to another
while KEEP_RUNNING:
  try:
    paths = input('File Path: ').split(' ')

    print(paths)

    for path in paths:
      origin = Path(PATH_OLD_PROJECT + path)
      destination = Path(PATH_PROJECT + path)

      if not origin.is_file():
        raise Exception('Origin file not found')

      destination.parent.mkdir(parents=True, exist_ok=True)

      final_dest = shutil.copy(origin, destination)
      print(final_dest)

  except KeyboardInterrupt:
    KEEP_RUNNING = False
  except Exception as e:
    print(f'Unexpected Error: {e}')

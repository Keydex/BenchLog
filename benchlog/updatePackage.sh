rm -rf dist
rm -rf benchlog.egg-info
python3 setup.py sdist
twine upload dist/*

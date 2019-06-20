# Homebrew-Formulae

Homebrew is known as "The missing package manager for macOS (or Linux)"

As a user, there is a lack of analytics to show the popularity of the packages installed by users using Homebrew which could vastly help users pick out the best packages for their needs. 
This project is based on that issue and contains python scripts that will grab data from a JSON API, parse out the information needed (using sleep to avoid slamming the server with multiple requests) 

```python
time.sleep(r.elapsed.total_seconds())
```

and then sort out the data based on popularity using a custom key.

[Homebrew Home Page](https://brew.sh/)
[Homebrew Packages](https://formulae.brew.sh/formula/)

## Information on files

### Data Script

This python script uses the request library to receive data from the JSON API listed on Homebrew and dumps the necessary information in the example package info file.

### Sort Script

This python script then sorts the information from the package info file depending on user needs. In this particular script, I look for packages with "video" mentioned and sorted by popularity. One can change the list comprehension 

```python
data = [item for item in data if 'video' in item['desc']]
```

to suit their particular needs.




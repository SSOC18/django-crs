# django-crs
Django application and models mirroring the CRS schema

The library used to convert the xsd files to django models is [generateDS](http://www.davekuhlman.org/generateDS.html).

**To use the library you need to:**
- [Download](https://sourceforge.net/projects/generateds/) the source distribution of the library.
- Extract it and open the django folder `.../Downloads/generateDS-2.29.24/django`.
- Paste your xsd files you want to convert into the django folder.
- Copy the process_includes.py file from `.../Downloads/generateDS-2.29.24/ and paste it into the django folder`.
- cd into the django folder and run the command: `python gends_run_gen_django.py <xsdfilename>.xsd`.
- Copy the generated files `models.py`, `forms.py` and `admin.py` into your django app.

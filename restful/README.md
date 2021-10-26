
<h2>About RESTful Hosting</h2>

Notes on pulling the project list display into static HTML page</h2>

Use the following API call:<br>
<a href="https://www.democracylab.org/api/projects?page=2&sortField=-project_date_modified">https://www.democracylab.org/api/projects?page=2&sortField=-project_date_modified</a><br><br>

Current API test page:<br>
<a href="https://model.earth/io/template/feed/demolab.html">Loren has requested header authentication key from Marlon</a><br><br>

Optionally use the following HTML template:<br>
<a href="common/components/common/projects/ProfileProjectSearch.jsx">common/components/common/projects/ProfileProjectSearch.jsx</a><br><br>


<h2>Install locally</h2>

If you do not yet have a .env file, copy the example.env file.<br><br>

<!--
We may NOT need to run the following to install locally for REST page setup:<br><br>

python3 -m venv .env<br>
source .env/bin/activate<br>
-->
	pip install -r requirements.txt

If you are not running Postgresql locally, you may need to remove these two lines in requirements.txt:<br><br>

	psycopg2==2.8.4
	psycopg2-binary==2.8.4

Run to activate local Postgres database

	sudo docker-compose exec web python3 manage.py flush --noinput
	sudo docker-compose exec web python3 manage.py loaddata testdata.json

<!--
Otherwise resulted in error:<br><br>

<code style="color:#333">
Running setup.py install for psycopg2 ... error<br>
ERROR: Command errored out with exit status 1:
 command: /Users/helix/Library/Data/CivicTechExchange/.env/bin/python3 -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/3m/rk27x_md7r14rv8rp44gm0900000gn/T/pip-install-albr4jgu/psycopg2/setup.py'"'"'; __file__='"'"'/private/var/folders/3m/rk27x_md7r14rv8rp44gm0900000gn/T/pip-install-albr4jgu/psycopg2/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record /private/var/folders/3m/rk27x_md7r14rv8rp44gm0900000gn/T/pip-record-zwe6rkbk/install-record.txt --single-version-externally-managed --compile --install-headers /Users/helix/Library/Data/CivicTechExchange/.env/include/site/python3.8/psycopg2
     cwd: /private/var/folders/3m/rk27x_md7r14rv8rp44gm0900000gn/T/pip-install-albr4jgu/psycopg2/
</code>
-->

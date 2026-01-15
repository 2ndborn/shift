## Deployment to Railway
1. Go to [Render.com](https://render.com/) and log in.
2. Create a new Railway Project.
	* Click **New Project**.
	* Choose **Deploy from GitHub repo**.
	* Select your Django project.
3. Add a Postgres database (Inside the project)
	-   Click **+ Add**
	-   Choose **Database**
	-   Select **PostgreSQL**
4. Add your environment variables (Go to)	
	| Name | Value |
	| - |- |
	| `Django settings`|  |
	| SECRET_KEY | your-secret-key |
	| DEBUG| False |
	| ALLOWED_HOST| your-railway-domain.up.railway.app
	 | `AWS/S3 settings`| |
	| USE_AWS| True|
	| AWS_ACCESS_KEY_ID| xxxx|
	| AWS_SECRET_ACCESS_KEY| xxxx|
	| AWS_STORAGE_BUCKET_NAME| your-bucket-name|
	| AWS_S3_REGION_NAME| your-region|
	| `STRIPE settings`| |
	| STRIPE_PUBLIC_KEY| xxxx|
	| STRIPE_SECRET_KEY| xxxx|
	| STRIPE_WH_SECRET| xxxx|
	| `EMAIL settings`| |
	| EMAIL_HOST_PASS| xxxx|
	| EMAIL_HOST_KEY| xxxx|
	
5. `Railway` go to
	* Railway> Web> Variables
	* Add

	| NAME| VALUE|
	| -- | -- |
	| DATABASE_URL| postgres://<your-full-connection-string>|		 
6. Change **ALLOW_HOSTS** & **DEBUG** variables in `settings.py` to:
	<div style="background:#f6f8fa; padding:1em; border-radius:6px;">
	  <pre><code>
	DEBUG  =  os.environ.get('DEBUG', 'False') ==  'True'
	ALLOWED_HOSTS  =  os.environ.get('ALLOWED_HOSTS', '127.0.0.1').split(',')
   </code></pre>
	</div>
7.  Configure the Database
	In `settings.py` change this code:
		<div style="background:#f6f8fa; padding:1em; border-		radius:6px;">
	  <pre><code>
	  DATABASES = {
		'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
	  }
	</code></pre>
	</div>
	For this code:
	<div style="background:#f6f8fa; padding:1em; border-radius:6px;">
	  <pre><code>
	  DATABASES  = {
		'default': dj_database_url.parse(
		os.environ.get("DATABASE_URL"),
		conn_max_age=600,
		ssl_require=True
		)
	  }
	</code></pre>
	</div>
8. Export data catalog as a fixture:
	<div style="background:#f6f8fa; padding:1em; border-radius:6px;">
	<pre><code>
		python manage.py dumpdata products > products.json
	</code></pre>
	</div>
10. Push to github **(This will automatically trigger your first deploy)**.

### Railway Pro Plan vs Hobby Plan
Once Railway has finished building:
If on Pro Plan follow these steps:
1. Go to your Railway dashboard
2. Open the **Shell** for your web service.
3. Run:
	<div style="background:#f6f8fa; padding:1em; border-radius:6px;">
		<pre><code>
		python3 manage.py migrate
		</code></pre>
	</div>
	Then:
	<div style="background:#f6f8fa; padding:1rem; border-radius:6px;">
	<pre><code>
		python manage.py loaddata products.json
	</code></pre>
	</div>
	Your live site should now have:
-  	All your products
-   Categories
-   Reviews
-   S3-hosted images

If on Hobby Plan follow these steps in the `products app`:

1.  Create this file path:
	<div style="background:#f6f8fa; padding:1em; border-radius:6px;">
			  <pre><code>
		products/management/commands/load_fixture.py
			  </code></pre>
	</div>
		  
2. Paste in this code:
	<div style="background:#f6f8fa; padding:1em; border-radius:6px;">
		<pre><code>
	  from  django.core.management.base import BaseCommand
	  from  django.core.management  import  call_command
	  class  Command(BaseCommand):
			help  =  'Load product fixture into the database'
			def  handle(self, *args, **kwargs):
				call_command('loaddata', 'products.json')
				self.stdout.write(self.style.SUCCESS('Product fixture loaded successfully.'))
		</code></pre>
	</div>

3. Add these 2 file paths and leave the __init__.py files empty:
	<div style="background:#f6f8fa; padding:1em; border-radius:6px;">
	<pre><code>
		products/management/__init__.py
		products/management/commands/__init__.py
	</code></pre>
	</div>
	
4. In the `products/views.py` paste in the code:
	<div style="background:#f6f8fa; padding:1em; border-radius:6px;">
	 <pre><code>
		from django.http import HttpResponse
		from django.core.management import call_command
		def run_fixture(request):
		    try:
		        call_command('load_fixture')
		        return HttpResponse("Fixture loaded.")
		    except Exception as e:
		        return HttpResponse(f"Error: {e}", status=500)
	        </code></pre>
		</div>
	<div style="background:#f6f8fa; padding:1em; border-radius:6px;">
	<pre><code>
		from django.http import HttpResponse
		from django.core.management import call_command
		def run_migrations(request):
		    try:
		        call_command('migrate')
		        return HttpResponse("Migrations applied.")
		    except Exception as e:
		        return HttpResponse(f"Error: {e}", status=500)
		</code></pre>
	</div>
		
5. In the `products/urls.py` paste in this code:
	<div style="background:#f6f8fa; padding:1em; border-radius:6px;">
	<pre><code>
		from django.urls import path
		from .views import run_fixture
		urlpatterns = [
		    path('run-fixture/', views.run_fixture),
		    path('run-migrations/', views.run_migrations),
		]
	</code></pre>
	</div>

6. Push your changes to GitHub.
7. Run the Migrations using this URL (You should see **Migrations applied.**):
	<div style="background:#f6f8fa; padding:1em; border-radius:6px;">
	<pre><code>https://web-production-402df.up.railway.app/products/run-migrations/
	</code></pre></div>

8. Run Fixtures using this URL(You should see **Fixture loaded.**):
	<div style="background:#f6f8fa; padding:1em; border-radius:6px;">
	<pre><code>https://web-production-402df.up.railway.app/products/run-migrations/
	</code></pre></div>
	
9. Remove temporary views and urls.
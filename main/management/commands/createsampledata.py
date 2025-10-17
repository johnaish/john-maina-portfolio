from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from main.models import Profile, Project, Post
from django.core.files.base import ContentFile
import urllib.request
from django.conf import settings
import os

class Command(BaseCommand):
    help = 'Create a sample superuser and some sample content'

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')
            self.stdout.write(self.style.SUCCESS('Created superuser: admin / adminpass'))
        else:
            self.stdout.write('Superuser admin already exists')

        if not Profile.objects.exists():
            p = Profile.objects.create(name='John Maina', tagline='IT Student & Visual Creator', bio='I study IT at the University of Embu. I build projects and design graphics.')
            # try to download a placeholder image
            try:
                url = 'https://via.placeholder.com/400x400.png?text=John+Maina'
                data = urllib.request.urlopen(url).read()
                p.photo.save('john_placeholder.png', ContentFile(data))
                p.save()
                self.stdout.write(self.style.SUCCESS('Profile created with placeholder image'))
            except Exception as e:
                self.stdout.write('Created profile without image: ' + str(e))
        else:
            self.stdout.write('Profile already exists')

        if not Project.objects.exists():
            for i in range(1,5):
                proj = Project.objects.create(title=f'Sample Project {i}', description='This is a sample project.', category='Design', featured=(i%2==0))
                try:
                    url = f'https://via.placeholder.com/800x600.png?text=Project+{i}'
                    data = urllib.request.urlopen(url).read()
                    proj.image.save(f'project_{i}.png', ContentFile(data))
                    proj.save()
                except Exception as e:
                    self.stdout.write('Could not download image: ' + str(e))
            self.stdout.write(self.style.SUCCESS('Sample projects created'))
        else:
            self.stdout.write('Projects already exist')

        if not Post.objects.exists():
            for i in range(1,3):
                Post.objects.create(title=f'Welcome Post {i}', content='This is a sample post to show the blog.')
            self.stdout.write(self.style.SUCCESS('Sample posts created'))
        else:
            self.stdout.write('Posts already exist')

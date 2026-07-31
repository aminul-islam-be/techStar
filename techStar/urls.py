from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

# হোম ভিউ
def home(request):
    return HttpResponse("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>TechStar Marketplace</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    max-width: 800px;
                    margin: 50px auto;
                    padding: 20px;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    text-align: center;
                }
                .container {
                    background: rgba(255,255,255,0.1);
                    padding: 40px;
                    border-radius: 20px;
                    backdrop-filter: blur(10px);
                }
                h1 { font-size: 3em; margin-bottom: 10px; }
                .subtitle { font-size: 1.2em; opacity: 0.9; }
                .links {
                    margin-top: 30px;
                    display: flex;
                    gap: 20px;
                    justify-content: center;
                    flex-wrap: wrap;
                }
                .btn {
                    display: inline-block;
                    padding: 12px 30px;
                    background: white;
                    color: #764ba2;
                    text-decoration: none;
                    border-radius: 30px;
                    font-weight: bold;
                    transition: transform 0.3s;
                }
                .btn:hover {
                    transform: scale(1.05);
                }
                .status {
                    margin-top: 30px;
                    padding: 15px;
                    background: rgba(255,255,255,0.2);
                    border-radius: 10px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🚀 TechStar</h1>
                <p class="subtitle">International Electrical & Electronics E-commerce Platform</p>
                <div class="links">
                    <a href="/admin" class="btn">🔐 Admin Panel</a>
                    <a href="https://github.com/aminul-isl/techStar" class="btn">📦 GitHub</a>
                </div>
                <div class="status">
                    ✅ Server is running successfully!<br>
                    <small>Django + Vercel Deployment</small>
                </div>
            </div>
        </body>
        </html>
    """)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
]

# ডেভেলপমেন্টে মিডিয়া/স্ট্যাটিক ফাইল সার্ভ করা
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

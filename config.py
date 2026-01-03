"""
Configuration for St. George's Biology Class LMS
"""
import os

class Config:
    """Base configuration"""
    # Secret key for session management
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'st-georges-biology-secret-key-change-in-production'

    # Database URI - SQLite by default, PostgreSQL-ready
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///biology_lms.db'

    # Track modifications (disable for performance)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # File upload settings
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024  # 50MB max file size

    # Allowed file extensions for library
    ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx', 'ppt', 'pptx', 'mp4', 'mp3', 'wav', 'jpg', 'jpeg', 'png', 'gif'}

    # Live class settings
    LIVE_CLASS_DURATION_MINUTES = 60

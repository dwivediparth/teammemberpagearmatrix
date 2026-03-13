"""Seed the database with sample team members."""
from database import SessionLocal, engine, Base
from models import TeamMember


SEED_DATA = [
    {
        "name": "Aarav Mehta",
        "role": "CEO & Co-Founder",
        "bio": "Aarav leads the vision at Armatrix, bringing 8+ years of experience in robotics and deep-tech startups. He holds an MS in Mechanical Engineering from IIT Bombay and is passionate about making hazardous industrial environments safer through autonomous systems.",
        "photo_url": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&h=400&fit=crop&crop=face",
        "linkedin_url": "https://linkedin.com/in/",
        "twitter_url": "https://twitter.com/",
        "order": 1,
    },
    {
        "name": "Priya Sharma",
        "role": "CTO & Co-Founder",
        "bio": "Priya architects the core control systems behind Armatrix's snake-like robotic arms. With a PhD in Control Systems from MIT, she leads the R&D team in developing AI-powered navigation for hyper-redundant manipulators.",
        "photo_url": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=400&h=400&fit=crop&crop=face",
        "linkedin_url": "https://linkedin.com/in/",
        "twitter_url": "https://twitter.com/",
        "order": 2,
    },
    {
        "name": "Rohan Kapoor",
        "role": "VP of Engineering",
        "bio": "Rohan oversees hardware and firmware development, ensuring every prototype meets rigorous safety and performance standards. Previously an engineering lead at ISRO, he brings deep expertise in mechatronics and embedded systems.",
        "photo_url": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=400&h=400&fit=crop&crop=face",
        "linkedin_url": "https://linkedin.com/in/",
        "twitter_url": "",
        "order": 3,
    },
    {
        "name": "Ananya Iyer",
        "role": "Head of AI & Perception",
        "bio": "Ananya develops the real-time computer vision and AI navigation stack that allows Armatrix arms to autonomously traverse complex industrial geometries. She previously worked at DeepMind on robotic manipulation research.",
        "photo_url": "https://images.unsplash.com/photo-1580489944761-15a19d654956?w=400&h=400&fit=crop&crop=face",
        "linkedin_url": "https://linkedin.com/in/",
        "twitter_url": "https://twitter.com/",
        "order": 4,
    },
    {
        "name": "Vikram Singh",
        "role": "Lead Mechanical Engineer",
        "bio": "Vikram designs the modular actuator assemblies and end-effectors that give Armatrix arms their versatility. With experience across aerospace and industrial automation, he turns ambitious CAD models into production-ready hardware.",
        "photo_url": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=400&h=400&fit=crop&crop=face",
        "linkedin_url": "https://linkedin.com/in/",
        "twitter_url": "",
        "order": 5,
    },
    {
        "name": "Neha Gupta",
        "role": "Head of Business Development",
        "bio": "Neha drives partnerships with major oil & gas, power, and infrastructure companies. She brings a decade of enterprise sales experience and was instrumental in closing Armatrix's $2.1M pre-seed round led by pi Ventures.",
        "photo_url": "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=400&h=400&fit=crop&crop=face",
        "linkedin_url": "https://linkedin.com/in/",
        "twitter_url": "https://twitter.com/",
        "order": 6,
    },
]


def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        if db.query(TeamMember).count() == 0:
            for member_data in SEED_DATA:
                db.add(TeamMember(**member_data))
            db.commit()
            print(f"✓ Seeded {len(SEED_DATA)} team members")
        else:
            print("Database already seeded, skipping.")
    finally:
        db.close()


if __name__ == "__main__":
    seed()

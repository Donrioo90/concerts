# tests/test_models.py
import pytest
from app import SessionLocal, engine
from models import Base, Band, Venue, Concert

@pytest.fixture(scope='module')
def session():
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)

def test_concert_relationships(session):
    band = Band(name="The Rolling Stones", hometown="London")
    venue = Venue(title="O2 Arena", city="London")
    concert = Concert(band=band, venue=venue, date="2024-10-10")
    session.add_all([band, venue, concert])
    session.commit()

    assert concert.band == band
    assert concert.venue == venue

def test_band_venues(session):
    band = Band(name="The Beatles", hometown="Liverpool")
    venue = Venue(title="Anfield", city="Liverpool")
    concert = Concert(band=band, venue=venue, date="2024-12-12")
    session.add_all([band, venue, concert])
    session.commit()

    assert venue in band.venues()

def test_concert_introduction(session):
    band = Band(name="Coldplay", hometown="London")
    venue = Venue(title="Wembley Stadium", city="London")
    concert = Concert(band=band, venue=venue, date="2024-11-11")
    session.add_all([band, venue, concert])
    session.commit()

    intro = concert.introduction()
    assert intro == "Hello London!!!!! We are Coldplay and we're from London"

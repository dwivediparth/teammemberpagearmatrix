from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models import TeamMember
from schemas import TeamMemberCreate, TeamMemberUpdate, TeamMemberResponse

router = APIRouter(prefix="/api/team", tags=["Team Members"])


@router.get("/", response_model=List[TeamMemberResponse])
def get_all_members(db: Session = Depends(get_db)):
    """Fetch all team members, ordered by the 'order' field."""
    members = db.query(TeamMember).order_by(TeamMember.order).all()
    return members


@router.get("/{member_id}", response_model=TeamMemberResponse)
def get_member(member_id: int, db: Session = Depends(get_db)):
    """Fetch a single team member by ID."""
    member = db.query(TeamMember).filter(TeamMember.id == member_id).first()
    if not member:
        raise HTTPException(status_code=404, detail="Team member not found")
    return member


@router.post("/", response_model=TeamMemberResponse, status_code=201)
def create_member(member: TeamMemberCreate, db: Session = Depends(get_db)):
    """Create a new team member."""
    db_member = TeamMember(**member.model_dump())
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member


@router.put("/{member_id}", response_model=TeamMemberResponse)
def update_member(member_id: int, member: TeamMemberUpdate, db: Session = Depends(get_db)):
    """Update an existing team member."""
    db_member = db.query(TeamMember).filter(TeamMember.id == member_id).first()
    if not db_member:
        raise HTTPException(status_code=404, detail="Team member not found")

    update_data = member.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_member, key, value)

    db.commit()
    db.refresh(db_member)
    return db_member


@router.delete("/{member_id}", status_code=204)
def delete_member(member_id: int, db: Session = Depends(get_db)):
    """Delete a team member."""
    db_member = db.query(TeamMember).filter(TeamMember.id == member_id).first()
    if not db_member:
        raise HTTPException(status_code=404, detail="Team member not found")
    db.delete(db_member)
    db.commit()
    return None

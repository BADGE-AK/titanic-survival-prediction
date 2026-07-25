from pydantic import BaseModel, Field


class PassengerData(BaseModel):
    pclass: int = Field(..., ge=1, le=3, description="Passenger class (1, 2, or 3)")
    sex: int = Field(..., ge=0, le=1, description="0 = Male, 1 = Female")
    age: float = Field(..., ge=0, description="Passenger age")
    sibsp: int = Field(..., ge=0, description="Number of siblings/spouses aboard")
    parch: int = Field(..., ge=0, description="Number of parents/children aboard")
    fare: float = Field(..., ge=0, description="Ticket fare")
    embarked: int = Field(..., ge=0, le=2, description="0 = S, 1 = C, 2 = Q")
    alone: int = Field(..., ge=0, le=1, description="0 = Not Alone, 1 = Alone")
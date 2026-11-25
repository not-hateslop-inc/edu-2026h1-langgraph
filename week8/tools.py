from langchain_core.tools import tool

ROOMS = {"A": ("4층 대회의실", 12), "B": ("4층 소회의실", 6), "C": ("5층 세미나실", 30)}

@tool
def find_room(people: int) -> str:
    """인원 수에 맞는 가장 작은 사내 회의실을 찾는다."""
    for k, (name, cap) in sorted(ROOMS.items(), key=lambda x: x[1][1]):
        if cap >= people:
            return f"{k}: {name} ({cap}인)"
    return "수용 가능한 회의실 없음"

@tool
def book_room(room: str, date: str) -> str:
    """회의실을 예약한다. room은 A/B/C, date는 YYYY-MM-DD."""
    return f"{date} {room} 회의실 예약 완료 (실습용 가짜 예약)"

TOOLS = [find_room, book_room]

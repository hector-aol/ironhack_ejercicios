# test.py
from vikingsClasses import Soldier, Viking, Saxon, War

def test_soldier():
    s = Soldier(100, 10)
    damage = s.receiveDamage(30)
    assert s.health == 70
    print("Soldier test passed!")

def test_viking():
    v = Viking("Ragnar", 100, 15)
    result = v.receiveDamage(30)
    assert "Ragnar has received 30 points of damage" in result
    print("Viking test passed!")

if __name__ == "__main__":
    test_soldier()
    test_viking()
    print("All tests passed!")
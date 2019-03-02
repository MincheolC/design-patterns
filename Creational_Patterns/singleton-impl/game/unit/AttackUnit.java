package game.unit;

public class AttackUnit extends GameUnit {

	private AttackUnit() {
	};

	public static GameUnit createInstance() {
		for (int i = 0; i < N_UNIT; i++) {
			if (pUnitArray[i] == null) {
				pUnitArray[i] = new AttackUnit();
				return pUnitArray[i];
			}
		}
		return null;
	}

}

package game.unit;

public class ProtectUnit extends GameUnit {

	private ProtectUnit() {
	};

	public static GameUnit createInstance() {
		for (int i = 0; i < N_UNIT; i++) {
			if (pUnitArray[i] == null) {
				pUnitArray[i] = new ProtectUnit();
				return pUnitArray[i];
			}
		}
		return null;
	}
}

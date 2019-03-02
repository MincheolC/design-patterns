package game.unit;

public abstract class GameUnit {
	protected static final int N_UNIT = 5;
	protected static GameUnit[] pUnitArray;
	
	protected GameUnit(){}

	public static GameUnit createInstance() {
		return null;
	};

	public static void initUnitArray() {
		pUnitArray = new GameUnit[N_UNIT];
	}

	public static void destroyUnit(GameUnit pUnit) {
		for (int i = 0; i < N_UNIT; i++) {
			if (pUnitArray[i] == pUnit) {
				pUnitArray[i] = null;
				return;
			}
		}
	}
}

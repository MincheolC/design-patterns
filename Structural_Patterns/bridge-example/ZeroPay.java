package function;

import function.impl.SimplePayImpl;

public class ZeroPay extends SimplePay {
	String accountID = "1234567";

	@Override
	public void execute() {
		SimplePayImpl imp = getSimplePayImpl();
		if (imp != null) {
			imp.startApp("ZERO PAY");
			imp.enterAccount(accountID);
			imp.pay(1000);
		}
	}

}

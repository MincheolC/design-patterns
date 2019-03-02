package function;

import function.impl.SimplePayImpl;

public class SamsungPay extends SimplePay {

	@Override
	public void execute() {
		SimplePayImpl imp = getSimplePayImpl();
		if (imp != null) {
			imp.startApp("Samsung pay");
			imp.authorize();
			imp.pay(1000);
		}
	}

}

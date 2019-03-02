package function;

import function.impl.SimplePayImpl;

public class Payco extends SimplePay {

	@Override
	public void execute() {
		SimplePayImpl imp = getSimplePayImpl();
		if (imp != null) {
			imp.startApp("PAYCO");
			imp.authorize();
			imp.pay(1000);
		}
	}
}

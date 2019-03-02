package function.test;

import java.util.ArrayList;
import java.util.List;

import org.junit.Test;

import function.SimplePay;
import function.SamsungPay;
import function.ZeroPay;
import function.Payco;

public class FunctionTest {

	@Test
	public void test() {
		List<SimplePay> windows = new ArrayList<SimplePay>();
		windows.add(new SamsungPay().setImpl(SimplePay.TYPE_GALAXY));
		windows.add(new Payco().setImpl(SimplePay.TYPE_GALAXY));
		windows.add(new ZeroPay().setImpl(SimplePay.TYPE_GALAXY));
		windows.add(new SamsungPay().setImpl(SimplePay.TYPE_IPHONE));
		windows.add(new Payco().setImpl(SimplePay.TYPE_IPHONE));
		windows.add(new ZeroPay().setImpl(SimplePay.TYPE_IPHONE));

		windows.stream().forEach(w -> {
			w.start();
			w.execute();
		});
	}

}

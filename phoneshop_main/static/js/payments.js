console.log("Hello world");

fetch("/payments/config/")
	.then((result) => {
		console.log("-- fetch config -- ");
		console.log(result);
		return result.json();
	})
	.then((data) => {
		console.log("-- inside data --");
		console.log(data);
		const stripe = Stripe(data.publicKey);

		document.querySelector("#checkoutBtn").addEventListener("click", () => {
			// Get checkout session ID
			fetch("/payments/create-checkout-session/")
				.then((result) => {
					return result.json();
				})
				.then((data) => {
					console.log(data);
					// Redirect to Stripe Checkout
					return stripe.redirectToCheckout({
						sessionId: data.sessionId,
					});
				})
				.then((result) => {
					console.log(result);
				});
		});
	});

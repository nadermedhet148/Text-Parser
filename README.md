**Text Parser**

This projectIs for get values from text By compare it to similar Text as template

**Features**

- Get values from text 
- Get similarity percentage for the two text 

**Example**

**Text** :
> 	Your Credit Card ****3933 had a Successful transaction of EGP 203.15 @ORANGE KARGO MALL,your available bal.EGP20.28 for lost/stolen card call 19700

**Template** : 

>	 Your Credit Card ****$card had a Successful transaction of $AmountCurrency $amount $beneficiary ,your available bal.$BalanceCurrency$balance for lost/stolen card call 19700

**Returned values **

> 	{
	'$AmountCurrency': 'EGP',
	'$BalanceCurrency': 'EGP',
	'$amount': '203.15',
	'$balance': '20.28',
	'$beneficiary': 'ORANGE KARGO MALL', '
	$card': '3933'
	}


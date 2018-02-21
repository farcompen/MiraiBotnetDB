# MiraiBotnetDB
<img src="mirai.jpg">

# Gettin Started
MiraiBotbet DB Project has <b>120K+</b> Unique Ip adresses in Database with ASN, IpAdress, FirstSeenDate and Ip Location  </br>
Database is going to be Updateded weekly. Last seen date is updated as 07 Feb. 2018 </br>

# How to Use 
<i>git clone https://github.com/farcompen/MiraiBotnetDB </br>
 cd MiraiBotnetDB/ </br>
 python3 Python/MiraiListPy.py </i>


# Authors

<b>Faruk GÜNGÖR</b> - <i>Computer Engineer</i> 

# License

Proje GPL v3.0 ile lisanslanmıştır



	<script src="http://code.jquery.com/jquery-1.10.2.min.js"></script>
	<script type="text/javascript">
		 // this is called when an error happens in a transaction
		function errorHandler(transaction, error) {
		    console.log('Error: ' + error.message + ' code: ' + error.code);

		}

		 // this is called when a successful transaction happens
		function successCallBack() {
		    console.log("DEBUGGING: success");

		}
		 //This is for Listing values present in the database
		function ListDBValues() {
		    $('#msgbox').html('');
		    var db = openDatabase('mydb-test', '1.0', 'sqllite test database', 2 * 1024 * 1024);
		    db.transaction(function (transaction) {
		        transaction.executeSql('SELECT * FROM Msg;', [],
		            function (transaction, result) {
		                if (result != null && result.rows != null) {
		                    console.log(result.rows)
		                    for (var i = 0; i < result.rows.length; i++) {
		                        var row = result.rows.item(i);
		                        console.log(row.Name)
		                        $('#msgbox').append('<br>' + row.MsgId + '. ' +
		                            row.Name + ' ' + row.Msg);
		                    }
		                }
		            }, errorHandler);
		    }, errorHandler, nullHandler);

		    return;
		}

		function nullHandler() {};
		$(document).ready(function () {
		    // Opening a existing database or creating a new one if don't exist
		    var db = openDatabase('mydb-test', '1.0', 'sqllite test database', 2 * 1024 * 1024);
		    db.transaction(function (tx) {
		        // Create a table in if not exist
		        tx.executeSql('CREATE TABLE IF NOT EXISTS Msg(MsgId INTEGER NOT NULL PRIMARY KEY, Name TEXT NOT NULL, Msg TEXT NOT NULL)', [], nullHandler, errorHandler);
		    }, errorHandler, successCallBack);
		});
		ListDBValues();
		$(document).on('click', '#submit', function () {
		    var db = openDatabase('mydb-test', '1.0', 'sqllite test database', 2 * 1024 * 1024);
		    db.transaction(function (tx) {
		        tx.executeSql('INSERT INTO Msg (Name, Msg) VALUES (?, ?)', [$('#name').val(), $('#msg').val()], nullHandler, errorHandler);
		    });
		    ListDBValues();
		})
	</script>


		<div id="msgbox">
		</div>
		<p>
			<input type="text" id="name" placeholder="Name" /></br>
			<input type="text" id="msg" placeholder="Message" /></br>
			<input type="button" value="Add Message" id="submit">
			<input type="button" value="Refresh" onClick="ListDBValues()"> <br

import web3, json
from web3 import exceptions
blockchain = web3.Web3(web3.Web3.HTTPProvider('Blockchain'))
Contract_address = web3.Web3.toChecksumAddress('0xa00fa5d9a857f62d72ff3361c0881d6309a084d1')
Contract_abi = json.loads('''[
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "address",
				"name": "Buyer",
				"type": "address"
			}
		],
		"name": "BuyerSet",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "string",
				"name": "_name",
				"type": "string"
			}
		],
		"name": "Itemadded",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "time",
				"type": "uint256"
			}
		],
		"name": "startend",
		"type": "event"
	},
	{
		"inputs": [],
		"name": "changeBuyer",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "changecangetmoney",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getback",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getcoin",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getinfo",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			},
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "setEnd",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_name",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "_price",
				"type": "uint256"
			}
		],
		"name": "setItem",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "setStart",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]''')
Contract_bytecode = "6080604052600060025560006003556000600460006101000a81548160ff02191690831515021790555034801561003557600080fd5b50336000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055506112d0806100856000396000f3fe60806040526004361061007b5760003560e01c80637338c4f71161004e5780637338c4f71461023c578063746a3aa81461025357806387a8bbad1461026a578063c0ad0fb6146102815761007b565b80631a2d86291461008057806328011aa81461014957806335975a3714610153578063389dc09b1461016a575b600080fd5b34801561008c57600080fd5b50610095610298565b60405180806020018781526020018681526020018581526020018481526020018373ffffffffffffffffffffffffffffffffffffffff168152602001828103825288818151815260200191508051906020019080838360005b838110156101095780820151818401526020810190506100ee565b50505050905090810190601f1680156101365780820380516001836020036101000a031916815260200191505b5097505050505050505060405180910390f35b6101516103c6565b005b34801561015f57600080fd5b5061016861076a565b005b34801561017657600080fd5b5061023a6004803603604081101561018d57600080fd5b81019080803590602001906401000000008111156101aa57600080fd5b8201836020820111156101bc57600080fd5b803590602001918460018302840111640100000000831117156101de57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f8201169050808301925050505050505091929192908035906020019092919050505061091e565b005b34801561024857600080fd5b50610251610b0f565b005b34801561025f57600080fd5b50610268610c2d565b005b34801561027657600080fd5b5061027f610de5565b005b34801561028d57600080fd5b50610296610f87565b005b606060008060008060006005600001600560010154600960003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054600254600354600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16858054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156103ab5780601f10610380576101008083540402835291602001916103ab565b820191906000526020600020905b81548152906001019060200180831161038e57829003601f168201915b50505050509550955095509550955095509550909192939495565b600560010154600960003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054340111801561042e575060011515600460009054906101000a900460ff161515145b801561048b57503373ffffffffffffffffffffffffffffffffffffffff16600560030160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1614155b6104fd576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252601c8152602001807f41756374696f6e20656e646564206f7220736d616c6c2070726963650000000081525060200191505060405180910390fd5b7ff7ef08bf87382352d9e3ff76db9f4e59aca917ba56ba9c288c383e76d70d63a233604051808273ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390a133600160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555034600960003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008282540192505081905550604051806080016040528060056000018054600181600116156101000203166002900480601f01602080910402602001604051908101604052809291908181526020018280546001816001161561010002031660029004801561067c5780601f106106515761010080835404028352916020019161067c565b820191906000526020600020905b81548152906001019060200180831161065f57829003601f168201915b50505050508152602001600960003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205481526020014281526020013373ffffffffffffffffffffffffffffffffffffffff16815250600560008201518160000190805190602001906107099291906111d8565b50602082015181600101556040820151816002015560608201518160030160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550905050565b60008054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff161461082b576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260138152602001807f43616c6c6572206973206e6f74206f776e65720000000000000000000000000081525060200191505060405180910390fd5b6000600354148015610851575060011515600460009054906101000a900460ff16151514155b6108c3576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252600d8152602001807f41756374696f6e20656e6465640000000000000000000000000000000000000081525060200191505060405180910390fd5b7f5b7050f8965d403978bb1821919f6c30991649d9df17a5d4880678d973532770426040518082815260200191505060405180910390a16001600460006101000a81548160ff02191690831515021790555042600281905550565b60008054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff16146109df576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260138152602001807f43616c6c6572206973206e6f74206f776e65720000000000000000000000000081525060200191505060405180910390fd5b600060025414610a57576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252600a8152602001807f4974656d2061646465640000000000000000000000000000000000000000000081525060200191505060405180910390fd5b60405180608001604052808381526020018281526020014281526020013373ffffffffffffffffffffffffffffffffffffffff1681525060056000820151816000019080519060200190610aac9291906111d8565b50602082015181600101556040820151816002015560608201518160030160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055509050505050565b600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff16148015610b7f575060001515600460009054906101000a900460ff161515145b8015610b9e575060001515600460019054906101000a900460ff161515145b610c10576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260138152602001807f41756374696f6e206f70656e206f72202e2e2e0000000000000000000000000081525060200191505060405180910390fd5b6001600460016101000a81548160ff021916908315150217905550565b60008054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614610cee576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260138152602001807f43616c6c6572206973206e6f74206f776e65720000000000000000000000000081525060200191505060405180910390fd5b60246005600201544203118015610d18575060011515600460009054906101000a900460ff161515145b610d8a576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260088152602001807f4e6f742074696d6500000000000000000000000000000000000000000000000081525060200191505060405180910390fd5b7f5b7050f8965d403978bb1821919f6c30991649d9df17a5d4880678d973532770426040518082815260200191505060405180910390a16000600460006101000a81548160ff02191690831515021790555042600381905550565b6000600960003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205414158015610e48575060001515600460009054906101000a900460ff161515145b610eba576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260138152602001807f57652073656e646564206974206265666f72650000000000000000000000000081525060200191505060405180910390fd5b3373ffffffffffffffffffffffffffffffffffffffff166108fc600960003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020549081150290604051600060405180830381858888f19350505050158015610f3f573d6000803e3d6000fd5b506000600960003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002081905550565b60008054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614611048576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260138152602001807f43616c6c6572206973206e6f74206f776e65720000000000000000000000000081525060200191505060405180910390fd5b60011515600460019054906101000a900460ff161515146110b4576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260258152602001806112766025913960400191505060405180910390fd5b3373ffffffffffffffffffffffffffffffffffffffff166108fc60096000600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020549081150290604051600060405180830381858888f1935050505015801561115b573d6000803e3d6000fd5b50600060096000600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000208190555060001515600460019054906101000a90505050565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061121957805160ff1916838001178555611247565b82800160010185558215611247579182015b8281111561124657825182559160200191906001019061122b565b5b5090506112549190611258565b5090565b5b80821115611271576000816000905550600101611259565b509056fe57652073656e646564206974206265666f7265206f7220796f752063616e27742074616b65a2646970667358221220011d3d70d608a1c6ab014d0be4638ec0701488b4881be05215f9fc5d0578cf9964736f6c63430007000033"
my_contract = blockchain.eth.contract(address=Contract_address, abi=Contract_abi)
admin_key = '0x2d745060f1050fa9557f4249f217e03f2d7d51e67cd3bec36159af461d5110ae'  # 0xb804b8a18C3F2ee4e3E4E96E6d3f3dc488c0A663
admin_address = '0xb804b8a18C3F2ee4e3E4E96E6d3f3dc488c0A663'

def additem(address, name, price):
    try:
        contract = blockchain.eth.contract(abi=Contract_abi, address=check(address))
        call_func = contract.functions.setItem(_name=name, _price=price).buildTransaction({
            'from': admin_address,
            'nonce': blockchain.eth.getTransactionCount(admin_address)})
        signed = blockchain.eth.account.sign_transaction(call_func, admin_key)
        tx_hash = blockchain.eth.send_raw_transaction(signed.rawTransaction)
        return ('Геш транзакції: ' + str(tx_hash.hex()))
    except exceptions.ContractLogicError as error:
        return ('Помилка: ' + str(error))


def check(address):
    try:
        return web3.Web3.toChecksumAddress(address)
    except:
        return 'Помилка, не правильно введено адресу'


def bet(address, user_address, user_key, client_bet):
    try:
        contract = blockchain.eth.contract(abi=Contract_abi, address=check(address))
        call_func = contract.functions.changeBuyer().buildTransaction({
            'from': user_address,
            'value': int(client_bet),
            'nonce': blockchain.eth.getTransactionCount(user_address)})
        signed = blockchain.eth.account.sign_transaction(call_func, user_key)
        tx_hash = blockchain.eth.send_raw_transaction(signed.rawTransaction)
        return ('Геш транзакції: ' + str(tx_hash.hex()))
    except exceptions.ContractLogicError as error:
        return ('Помилка: ' + str(error))
    except ValueError as error:
        return ('Сталась невідома помилка ' + str(error))


def start_auction(address):
    try:
        contract = blockchain.eth.contract(abi=Contract_abi, address=check(address))
        call_func = contract.functions.setStart().buildTransaction({
            'from': admin_address,
            'nonce': blockchain.eth.getTransactionCount(admin_address)})
        signed = blockchain.eth.account.sign_transaction(call_func, admin_key)
        tx_hash = blockchain.eth.send_raw_transaction(signed.rawTransaction)
        return ('Геш транзакції: ' + str(tx_hash.hex()))
    except exceptions.ContractLogicError as error:
        return ('Помилка: ' + str(error))


def end_auction(address):
    try:
        contract = blockchain.eth.contract(abi=Contract_abi, address=check(address))
        call_func = contract.functions.setEnd().buildTransaction({
            'from': admin_address,
            'nonce': blockchain.eth.getTransactionCount(admin_address)})
        signed = blockchain.eth.account.sign_transaction(call_func, admin_key)
        tx_hash = blockchain.eth.send_raw_transaction(signed.rawTransaction)
        return ('Геш транзакції: ' + str(tx_hash.hex()))
    except exceptions.ContractLogicError as error:
        return ('Помилка: ' + str(error))


def cash_back(address,user_address, user_key):
    try:
        contract = blockchain.eth.contract(abi=Contract_abi, address=check(address))
        call_func = contract.functions.getback().buildTransaction({
            'from': user_address,
            'nonce': blockchain.eth.getTransactionCount(user_address)})
        signed = blockchain.eth.account.sign_transaction(call_func, user_key)
        tx_hash = blockchain.eth.send_raw_transaction(signed.rawTransaction)
        return ('Геш транзакції: ' + str(tx_hash.hex()))
    except exceptions.ContractLogicError as error:
        return ('Помилка: ' + str(error))


def withdraw(address):
    try:
        contract = blockchain.eth.contract(abi=Contract_abi, address=check(address))
        call_func = contract.functions.getcoin().buildTransaction({
            'from': admin_address,
            'nonce': blockchain.eth.getTransactionCount(admin_address)})
        signed = blockchain.eth.account.sign_transaction(call_func, admin_key)
        tx_hash = blockchain.eth.send_raw_transaction(signed.rawTransaction)
        return ('Геш транзакції: ' + str(tx_hash.hex()))
    except exceptions.ContractLogicError as error:
        return ('Помилка: ' + str(error))


def can_withdraw(address, user_address, user_key):
    try:
        contract = blockchain.eth.contract(abi=Contract_abi, address=check(address))
        call_func = contract.functions.changecangetmoney().buildTransaction({
            'from': user_address,
            'nonce': blockchain.eth.getTransactionCount(user_address)})
        signed = blockchain.eth.account.sign_transaction(call_func, user_key)
        tx_hash = blockchain.eth.send_raw_transaction(signed.rawTransaction)
        return ('Геш транзакції: ' + str(tx_hash.hex()))
    except exceptions.ContractLogicError as error:
        return ('Помилка: ' + str(error))


def add_contact():
    try:
        new_contract = blockchain.eth.contract(abi=Contract_abi, bytecode=Contract_bytecode)
        trans = new_contract.constructor().buildTransaction({
                'from': admin_address,
                'nonce': blockchain.eth.getTransactionCount(admin_address)})
        signed = blockchain.eth.account.sign_transaction(trans, admin_key)
        tx_hash = blockchain.eth.send_raw_transaction(signed.rawTransaction)
        contract = blockchain.eth.wait_for_transaction_receipt(tx_hash)['contractAddress']
        return {'Tx_Hash': tx_hash.hex(), 'Contract_Address': contract}
    except exceptions.ContractLogicError as error:
        return ('Помилка: ' + str(error))


""" Отримання інформації зі смарт-контракту """


def get_info(user, contract_address):
    contract = blockchain.eth.contract(abi=Contract_abi, address=check(contract_address))
    if user is None:
        call_func = contract.functions.getinfo().call({})
    else:
        call_func = contract.functions.getinfo().call({'from': user['user_address']})
    return call_func


""" Події """


def item_info(address):
    contract =blockchain.eth.contract(abi=Contract_abi, address=check(address))
    event_filter = contract.events.Itemadded().createFilter(fromBlock="0x0")
    entry = event_filter.get_all_entries()[-1]
    trans= blockchain.eth.get_transaction(entry['transactionHash'])
    x=int(trans['input'][138:202].lstrip('0'))
    return str(entry['args']['_price']), bytearray.fromhex(trans['input'][202:(202+x*2)]).decode()


def auction_event(address, from_db):
    contract = blockchain.eth.contract(abi=Contract_abi, address=check(address))
    event_filter = contract.events.startend().createFilter(fromBlock="0x0")
    entries = event_filter.get_all_entries()
    if len(entries) != 0:
        if entries[-1]['args']['time'] != from_db:
            if len(entries) == 1:
                return {'Auction': "Аукціон розпочався", 'Ended': False, 'Time': entries[-1]['args']['time']}
            elif len(entries) == 2:
                return {'Auction': 'Аукціон закінчився', 'Ended': True, 'Time': entries[-1]['args']['time']}


def bet_event(address, from_db):
    contract = blockchain.eth.contract(abi=Contract_abi, address=check(address))
    event_filter = contract.events.BuyerSet().createFilter(fromBlock="0x0")
    entries = event_filter.get_all_entries()
    if len(entries) != 0:
        if entries[-1]['args']['Buyer'] != from_db:
            return {'Bet': "Ставку підвищили", 'Buyer': entries[-1]['args']['Buyer']}

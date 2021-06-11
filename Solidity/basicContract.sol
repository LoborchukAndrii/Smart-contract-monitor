// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract Auction {
    address private owner;
    address winner;
    uint start = 0;
    uint end = 0;
    bool open = false;
    bool cangetcoin;
    struct Item {
    string name;
    uint price;
    uint time;
    address buyer;}
    Item AuctionItem; 
    event startend(uint time);
    event BuyerSet(address Buyer);
    event Itemadded(string indexed _name);
    modifier isOwner() {
        require(msg.sender == owner, "Caller is not owner");
        _;}
    mapping (address=>uint) private balances;
    constructor() {
        owner = msg.sender;}
    function setitem(string memory _name, uint _price) public isOwner {
        require (start == 0, "Item added");
        AuctionItem=Item(_name, _price, block.timestamp, msg.sender);}
    function changeBuyer() public payable {
        require ( (msg.value + balances[msg.sender] ) > AuctionItem.price && open == true && AuctionItem.buyer != msg.sender, "Auction ended or small price");
        emit BuyerSet(msg.sender);
        winner = msg.sender;
        balances[msg.sender] += msg.value;
        AuctionItem=Item(AuctionItem.name, balances[msg.sender], block.timestamp, msg.sender);}
    function setStart() external isOwner {
        require(end == 0 && open != true, "Auction ended");
        emit startend(block.timestamp);
        open = true;
        start = block.timestamp;}
    function setEnd() external isOwner {
        require ( (block.timestamp - AuctionItem.time)  > 36 && open == true, "Not time");
        emit startend(block.timestamp);
        open = false;
        end = block.timestamp;}
    function getinfo() external view returns(string memory, uint, uint, uint, uint, address) {
        return (AuctionItem.name, AuctionItem.price, balances[msg.sender], start, end, winner);}
    function getcoin() external isOwner{
        require (cangetcoin == true, "We sended it before or you can't take");
        msg.sender.transfer(balances[winner]);
        balances[winner]=0;
        cangetcoin == false;
    }
    
    function changecangetmoney() external{
        require (msg.sender == winner && open == false && cangetcoin == false, "Auction open or ...");
        cangetcoin = true;
    }
    
    function getback() external{
        require (balances[msg.sender] != 0 && open == false, "We sended it before");
        msg.sender.transfer(balances[msg.sender]);
        balances[msg.sender]=0;
    }
}

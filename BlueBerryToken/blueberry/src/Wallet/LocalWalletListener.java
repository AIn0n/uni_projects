package Wallet;

import core.BlockChain.BlockChain;
import core.BlockChain.Blocks.StdBlock;
import core.MinimalMiner;
import Transaction.Transactions;
import Transaction.Tx;

public class LocalWalletListener implements WalletListener
{
    private final BlockChain blockChain;

    public LocalWalletListener(BlockChain bc) { this.blockChain = bc; }

    @Override
    public BlockChain getBlockChain() {
        return blockChain;
    }

    @Override
    public void sendTx(Tx tx)
    {
        StdBlock block = MinimalMiner.mine(new Transactions(tx), blockChain.last().getHash());
        this.blockChain.add(block);
    }

    @Override
    public byte[] getLastBlockHash() {
        return blockChain.last().getHash();
    }
}

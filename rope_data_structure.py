#!/usr/bin/env python3
"""Rope — balanced binary tree for efficient string operations."""
class RopeNode:
    def __init__(self,s=""):
        self.left=self.right=None;self.data=s;self.weight=len(s)
def rope_concat(left,right):
    if not left: return right
    if not right: return left
    n=RopeNode();n.left=left;n.right=right;n.weight=_len(left);return n
def _len(node):
    if not node: return 0
    if node.data: return len(node.data)
    return _len(node.left)+_len(node.right)
def rope_index(node,i):
    if node.data: return node.data[i]
    if i<node.weight: return rope_index(node.left,i)
    return rope_index(node.right,i-node.weight)
def rope_to_str(node):
    if not node: return ""
    if node.data: return node.data
    return rope_to_str(node.left)+rope_to_str(node.right)
def rope_split(node,i):
    if not node: return None,None
    if node.data:
        l=RopeNode(node.data[:i]);r=RopeNode(node.data[i:])
        return (l if l.data else None),(r if r.data else None)
    if i<=node.weight:
        ll,lr=rope_split(node.left,i)
        return ll,rope_concat(lr,node.right)
    rl,rr=rope_split(node.right,i-node.weight)
    return rope_concat(node.left,rl),rr
def main():
    a=RopeNode("Hello ");b=RopeNode("World!")
    r=rope_concat(a,b)
    print(f"String: {rope_to_str(r)}, char[6]: {rope_index(r,6)}")
if __name__=="__main__":main()

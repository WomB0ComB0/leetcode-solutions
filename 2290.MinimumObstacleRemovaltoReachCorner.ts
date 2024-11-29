class Heap {
  private heap: [number, number, number][] = [];

  constructor(x: [number, number, number][]) {
    this.heap = x;
    for (let i = Math.floor(this.heap.length / 2) - 1; i >= 0; i--) {
      this._siftDown(i);
    }
  }

  push(val: [number, number, number]) {
    this.heap.push(val);
    this._siftUp(this.heap.length - 1);
  }

  pop(): [number, number, number] {
    if (this.heap.length === 0) throw new Error("Heap is empty");
    
    const result = this.heap[0];
    const last = this.heap.pop()!;
    
    if (this.heap.length > 0) {
      this.heap[0] = last;
      this._siftDown(0);
    }
    
    return result;
  }

  private _siftUp(index: number) {
    while (index > 0) {
      const parentIndex = Math.floor((index - 1) / 2);
      if (this.heap[parentIndex][0] > this.heap[index][0]) {
        [this.heap[parentIndex], this.heap[index]] = [this.heap[index], this.heap[parentIndex]];
        index = parentIndex;
      } else {
        break;
      }
    }
  }

  private _siftDown(index: number) {
    const length = this.heap.length;
    while (true) {
      let smallest = index;
      const leftChild = 2 * index + 1;
      const rightChild = 2 * index + 2;

      if (leftChild < length && this.heap[leftChild][0] < this.heap[smallest][0]) {
        smallest = leftChild;
      }
      if (rightChild < length && this.heap[rightChild][0] < this.heap[smallest][0]) {
        smallest = rightChild;
      }

      if (smallest !== index) {
        [this.heap[index], this.heap[smallest]] = [this.heap[smallest], this.heap[index]];
        index = smallest;
      } else {
        break;
      }
    }
  }

  // ... keep existing size() and isEmpty() methods ...
}

// Remove the _shiftDown and _shiftUp standalone functions as they're now methods in the class
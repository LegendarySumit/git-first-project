<div align="center">

# 📐 Arrays & Sparse Matrix — Code Snippets

**Exam-oriented snippets covering array operations, sparse matrix, and address calculation**

![Data Structures](https://img.shields.io/badge/Data_Structures-Arrays-orange)
![Java](https://img.shields.io/badge/Java-007396?logo=java&logoColor=white)

*Formula clarity for exam success*

</div>

---

## 1️⃣ Array Creation (1D Array)
```java
int[] arr = new int[5];

// Initializing values
arr[0] = 10;
arr[1] = 20;
arr[2] = 30;
arr[3] = 40;
arr[4] = 50;
```

---

## 2️⃣ Array Traversal
```java
for (int i = 0; i < arr.length; i++) {
    System.out.println(arr[i]);
}
```

---

## 3️⃣ Array Insertion (At Specific Position)
```java
int[] arr = new int[10];
int n = 5; // current size

// existing elements
for (int i = 0; i < n; i++) {
    arr[i] = i + 1;
}

int pos = 2;   // position to insert (0-based)
int value = 99;

// shift elements
for (int i = n; i > pos; i--) {
    arr[i] = arr[i - 1];
}

// insert value
arr[pos] = value;
n++;
```

---

## 4️⃣ Array Deletion (From Specific Position)
```java
int pos = 2; // index to delete

for (int i = pos; i < n - 1; i++) {
    arr[i] = arr[i + 1];
}
n--;
```

---

## 5️⃣ Array Searching (Linear Search)
```java
int key = 30;
boolean found = false;

for (int i = 0; i < n; i++) {
    if (arr[i] == key) {
        System.out.println("Element found at index " + i);
        found = true;
        break;
    }
}

if (!found) {
    System.out.println("Element not found");
}
```

---

## 6️⃣ Sparse Matrix — Triplet Representation

### Example Matrix
```
0 0 3
0 0 0
5 0 0
```

### Code
```java
int[][] matrix = {
    {0, 0, 3},
    {0, 0, 0},
    {5, 0, 0}
};

int rows = 3;
int cols = 3;

// Count non-zero elements
int count = 0;
for (int i = 0; i < rows; i++) {
    for (int j = 0; j < cols; j++) {
        if (matrix[i][j] != 0) {
            count++;
        }
    }
}

// Triplet representation
int[][] sparse = new int[count + 1][3];

// First row: [rows, cols, count]
sparse[0][0] = rows;
sparse[0][1] = cols;
sparse[0][2] = count;

int k = 1;
for (int i = 0; i < rows; i++) {
    for (int j = 0; j < cols; j++) {
        if (matrix[i][j] != 0) {
            sparse[k][0] = i;      // row
            sparse[k][1] = j;      // column
            sparse[k][2] = matrix[i][j]; // value
            k++;
        }
    }
}
```

### Triplet Output
```
Row  Col  Value
3    3    2      (metadata: 3 rows, 3 cols, 2 non-zero)
0    2    3
2    0    5
```

---

## 7️⃣ Address Calculation — 1D Array

### Formula
```
Address(A[i]) = Base + (i × size)
```

### Example

**Given:**
- Base = 1000
- Size = 4 bytes
- i = 5

**Calculation:**
```
Address = 1000 + (5 × 4)
        = 1000 + 20
        = 1020
```

---

## 8️⃣ Address Calculation — 2D Array (Row Major Order)

### Formula
```
Address(A[i][j]) = Base + [(i × cols + j) × size]
```

### Example

**Given:**
- Base = 2000
- Rows = 3, Cols = 4
- i = 1, j = 2
- Size = 2 bytes

**Calculation:**
```
Address = 2000 + [(1×4 + 2) × 2]
        = 2000 + (6 × 2)
        = 2000 + 12
        = 2012
```

---

## 9️⃣ Address Calculation — 2D Array (Column Major Order)

### Formula
```
Address(A[i][j]) = Base + [(j × rows + i) × size]
```

### Example

**Given:**
- Base = 2000
- Rows = 3, Cols = 4
- i = 1, j = 2
- Size = 2 bytes

**Calculation:**
```
Address = 2000 + [(2×3 + 1) × 2]
        = 2000 + (7 × 2)
        = 2000 + 14
        = 2014
```

---

## 🔑 Exam Key Points (Don't Skip)

### Array Fundamentals
- ✅ Arrays use **contiguous memory**
- ✅ Insertion & deletion require **shifting elements**
- ✅ Linear search is **O(n)** time complexity
- ✅ Random access is **O(1)**

### Sparse Matrix
- ✅ Sparse matrix **saves space** when zeros dominate
- ✅ Triplet form: `[row, column, value]`
- ✅ First row stores metadata: `[rows, cols, count]`

### Address Calculation
- ✅ Address calculation depends on **storage order**
- ✅ **Row-major**: rows stored sequentially
- ✅ **Column-major**: columns stored sequentially
- ✅ **Formulas must be written clearly in exams**

---

## 📊 Time Complexity Summary

| Operation | Time Complexity |
|-----------|----------------|
| Access | O(1) |
| Search (Linear) | O(n) |
| Insertion | O(n) |
| Deletion | O(n) |
| Traversal | O(n) |

---

## 👨‍💻 Author

**Sumit**

- GitHub: [@LegendarySumit](https://github.com/LegendarySumit)

---

<div align="center">

**📐 Master the formulas, ace the exams**

*Array operations and address calculations made clear*

</div>
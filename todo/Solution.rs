impl Solution {
    pub fn remove_kdigits(num: String, mut k: i32) -> String {
        let num = num.chars().collect::<Vec<_>>();
        let mut stack = vec![];
        for n in num {
            while !stack.is_empty() && (k > 0 && *stack.last().unwrap() as i32 > n as i32) {
                stack.pop();
                k -= 1;
            }
            stack.push(n);
        }
        while k > 0 {
            stack.pop();
            k -= 1;
        }
        let stack = stack
            .into_iter()
            .skip_while(|x| *x == '0')
            .collect::<Vec<_>>();
        if stack.is_empty() {
            "0".to_string()
        } else {
            stack.into_iter().collect()
        }
    }
}
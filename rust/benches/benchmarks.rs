use criterion::{criterion_group, criterion_main, Criterion};

fn benchmark(_c: &mut Criterion) {
    // Add benchmarks here
}

criterion_group!(benches, benchmark);
criterion_main!(benches);

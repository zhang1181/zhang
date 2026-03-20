class Exercise:
    def __init__(self, name: str, target_reps: int):
        self.name = name
        self.target_reps = target_reps
        self.done_reps = 0
        self.completed = False

    def do(self, reps: int):
        if reps <= 0:
            raise ValueError("reps 必须是正数")
        if self.completed:
            return  # 已完成就不再累计

        self.done_reps += reps
        if self.done_reps >= self.target_reps:
            self.done_reps = self.target_reps
            self.completed = True

    def reset(self):
        self.done_reps = 0
        self.completed = False

    def progress(self) -> float:
        # 返回完成比例 0~1
        return self.done_reps / self.target_reps if self.target_reps else 0.0

    def status(self) -> str:
        if self.completed:
            return f"{self.name} 已完成！({self.done_reps}/{self.target_reps})"
        return f"{self.name} 进行中...({self.done_reps}/{self.target_reps})"


if __name__ == "__main__":
    ex = Exercise("俯卧撑", 20)
    print(ex.status())
    ex.do(6)
    print(ex.progress(), ex.status())
    ex.do(20)
    print(ex.status())

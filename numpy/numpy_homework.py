import numpy as np


def task_01():
    a = np.arange(60).reshape(3, 4, 5)
    print(f"{a.shape=} {a.ndim=} {a.size=} {a.dtype=} {a.strides=}")
    print("C_CONTIGUOUS =", a.flags.c_contiguous)
    print(f"Шаги {a.strides} задают смещения в байтах на один слой, строку и элемент соответственно .")
    print("В трёх слоях по четыре строки из пяти элементов, поэтому size = 3 × 4 × 5 = 60 .")


def task_02():
    a = np.array([1, 2, 3, 4])
    print("a / 2 =", a / 2, "   a // 2 =", a // 2, "   a / 2.0 =", a / 2.0)
    print("Типы a, a / 2, a // 2 =", a.dtype, (a / 2).dtype, (a // 2).dtype)
    b = np.array([1, 2, 3], dtype=np.int8)
    result = b + 127
    print("a =", a, "   b + 127 =", result, result.dtype)
    print("Деление создаёт новый массив, поэтому значения a сохраняются .")
    print("Сложение массива выполняется в int8: числа 128–130 выходят за диапазон и дают −128…−126 .")
    print("Целочисленная операция над массивом сохраняет младшие восемь бит без исключения .")


def task_03():
    error32 = float(np.float32(0.1)) - 0.1
    error64 = float(np.float64(0.1)) - 0.1
    for name, error in (("float32", error32), ("float64", error64)):
        print(f"{name}: {error!r}   {error:.20e}")
    print("Отношение ошибок не определено: знаменатель равен нулю, так как эталон 0.1 сам имеет точность float64 .")
    print("float32 подходит для приближённых расчётов, если ошибка укладывается в допуск .")
    print("При потере значащих цифр или решении плохо обусловленных систем может понадобиться float64 .")


def task_04():
    shape = (2, 3)
    for a in (np.zeros(shape, np.float64), np.zeros(shape, np.float32),
              np.ones(shape, np.int16), np.full(shape, 7, np.uint8)):
        print(a.dtype, a.nbytes, "байт")
    saved = 1000 * 1000 * (np.dtype(np.float64).itemsize - np.dtype(np.float32).itemsize)
    print("Экономия для (1000, 1000) =", saved, "байт")
    print("float32 занимает вдвое меньше памяти . У float64 больше значащих цифр .")


def task_05():
    a = np.arange(24)
    current = a
    for shape in ((4, 6), (2, 3, 4), (2, 2, 6), (24,)):
        current = current.reshape(shape)
        print(current.shape, np.array_equal(a, current.ravel()))
    print("Здесь reshape меняет форму и шаги, сохраняя общий буфер .")
    print("Копия нужна, когда существующие шаги не позволяют представить нужный порядок элементов .")


def task_06():
    M = np.arange(12).reshape(3, 4)
    f = M.flatten()
    r = M.ravel()
    print("f.base is None =", f.base is None, "   r.base is not None =", r.base is not None)
    f[0] = 999
    print("После f[0] = 999:", M, sep="\n")
    r[1] = 888
    print("После r[1] = 888:", M, sep="\n")
    print("flatten создаёт независимую копию для последующих изменений .")
    print("ravel экономит память, когда порядок элементов допускает представление без копирования .")


def task_07():
    v = np.arange(5)
    print(v[:, None].shape, "Добавлена ось столбца, в каждой строке одно число .")
    print(v[None, :].shape, "Добавлена ось строки, все числа лежат в одной строке .")
    print(np.squeeze(v[:, None]).shape, "Удалена ось длины 1 .")
    t = np.arange(6).reshape(2, 3).T
    print(t.shape, "Строки стали столбцами .", t, sep="\n")
    sums = v[:, None] + v[None, :]
    print(sums.shape, "Таблица сложения: элемент [i, j] равен i + j .", sums, sep="\n")


def task_08():
    A = np.arange(6).reshape(2, 3)
    B = A.T
    print("B.base is not None =", B.base is not None, "   strides:", A.strides, B.strides)
    B[0, 1] = 999
    print(A)
    print("Транспонирование меняет местами шаги осей и использует тот же буфер .")
    print("Поэтому запись в B[0, 1] изменила A[1, 0] .")


def task_09():
    A = np.arange(6).reshape(2, 3)
    B = np.arange(6).reshape(3, 2)
    for name, result in (("A @ B", A @ B), ("A.T @ B.T", A.T @ B.T), ("A * A", A * A)):
        print(name, result.shape, result, sep="\n")
    print("Оператор * перемножает элементы попарно: формы (2, 3) и (3, 2) несовместимы для broadcasting .")
    print("Оператор @ вычисляет скалярное произведение каждой строки слева с каждым столбцом справа .")
    d = np.diag([2, 3])
    print("d * d =", d * d, "d @ d =", d @ d, sep="\n")


def task_10():
    M = np.arange(12).reshape(3, 4)
    print(M.sum(axis=0), "axis=0: суммы по каждому столбцу .")
    print(M.sum(axis=1), "axis=1: суммы по каждой строке .")
    print(M.mean(axis=0), "axis=0: средние по каждому столбцу .")
    print(M.mean(axis=1), "axis=1: средние по каждой строке .")
    print(M.argmax(axis=0), "axis=0: индекс строки максимума каждого столбца .")
    print(M.argmax(axis=1), "axis=1: индекс столбца максимума каждой строки .")
    small = np.array([[1, 2, 3], [4, 5, 6]])
    print("Проверка [1+4, 2+5, 3+6]:", small.sum(axis=0), np.array_equal(small.sum(axis=0), [5, 7, 9]))


def task_11():
    X = np.random.default_rng(42).normal(size=(5, 3))
    for keep in (False, True):
        mean = X.mean(axis=0, keepdims=keep)
        std = X.std(axis=1, keepdims=keep)
        print("Средние столбцов:", mean, mean.shape, "   форма разности:", (X - mean).shape)
        print("Стандартные отклонения строк:", std, std.shape)
    z = (X - X.mean(axis=1, keepdims=True)) / X.std(axis=1, keepdims=True)
    print("Средние строк:", z.mean(axis=1), np.allclose(z.mean(axis=1), 0))
    print("Стандартные отклонения строк:", z.std(axis=1), np.allclose(z.std(axis=1), 1))
    print("keepdims сохраняет свёрнутую ось с длиной 1 .")
    print("Форма (5, 1) позволяет использовать отдельное среднее и отклонение для каждой из пяти строк .")


def task_12():
    a = np.arange(10)
    b = a[2:5]
    b[0] = 999
    print("После изменения среза:", a)
    c = a[2:5].copy()
    c[0] = -1
    print("После изменения копии:", a, "   копия:", c)
    print("Срез позволяет читать участок большого массива без дополнительной памяти под данные .")
    print("Если нормировать срез на месте, повторный эксперимент получит уже изменённые измерения .")
    print("Для независимой обработки участка нужна копия .")


def task_13():
    a = np.random.default_rng(0).normal(size=20)
    print("Положительных:", a[a > 0].size, "   между −1 и 1:", a[(a > -1) & (a < 1)].size)
    print("Элементы на позициях 0, 5, 10, 15:", a[[0, 5, 10, 15]])
    print("Выбросы:", a[np.abs(a) > 2])
    print("a[a > 0] содержит отобранные числа float, а (a < 1) — маску исходной длины .")
    print("Оператор & поэлементно объединяет две булевы маски одинаковой формы: (a > 0) & (a < 1) .")
    a[a < 0] = 0
    print("После замены:", a)


def task_14():
    X = np.random.default_rng(1).normal(size=(100, 3))
    X_norm = (X - X.mean(axis=0)) / X.std(axis=0)
    print("Средние:", X_norm.mean(axis=0), np.allclose(X_norm.mean(axis=0), 0))
    print("Стандартные отклонения:", X_norm.std(axis=0), np.allclose(X_norm.std(axis=0), 1))
    D = np.linalg.norm(X_norm[:, None, :] - X_norm[None, :, :], axis=2)
    print("Форма:", D.shape, D.shape == (100, 100))
    print("Нулевая диагональ:", np.allclose(D.diagonal(), 0), "   симметрия:", np.allclose(D, D.T))


def task_15():
    rng = np.random.default_rng(42)
    raw = rng.normal(20, 2, size=(30, 4))
    raw[7, 2] = 100
    print("Исходные данные:", raw.shape, raw.dtype, raw.size)
    mask = np.abs(raw - raw.mean(axis=0)) > 3 * raw.std(axis=0)
    print("Выбросов:", mask.sum(), "   индексы:", np.argwhere(mask).tolist(), "   значения:", raw[mask])
    marked = raw.copy()
    marked[mask] = np.nan
    means = np.nanmean(marked, axis=0)
    clean = np.where(np.isnan(marked), means, marked)
    print("Значения при замене:", marked[mask], "→", clean[mask], "   средние без выбросов:", means)
    transposed = clean.T
    restored = transposed.T
    print("Транспонирование:", transposed.shape, restored.shape, np.array_equal(clean, restored))
    flat = restored.ravel()
    restored = flat.reshape(30, 4)
    print("Развёртка и восстановление:", flat.shape, restored.shape, np.array_equal(clean, restored))
    means = restored.mean(axis=0)
    std = restored.std(axis=0)
    print("Средние датчиков:", means, "   стандартные отклонения:", std)
    z = (restored - means) / std
    print("Средние после нормировки:", z.mean(axis=0), np.allclose(z.mean(axis=0), 0))
    print("Стандартные отклонения:", z.std(axis=0), np.allclose(z.std(axis=0), 1))
    print("Копия перед записью NaN сохранила исходные измерения .")
    print("Маска, подстановка средних и нормировка используют broadcasting векторов по четырём датчикам .")
    print("Вектор средних по дням формы (30,) вызвал бы ошибку при вычитании из массива (30, 4) .")


def task_16():
    print("Xavier-rp, Stack Overflow: https://stackoverflow.com/q/46858376")
    print("Исходный фрагмент: xlist = np.arange(99995,99996)   →   print(xlist*xlist)")
    x = np.arange(99995, 99996, dtype=np.int32)
    print("До исправления (int32):", x * x)
    wide = x.astype(np.int64)
    print("После исправления (int64):", wide * wide)
    print("Квадрат 99995 превышает максимальное значение int32 .")
    print("Переход к int64 до умножения позволяет сохранить верный результат .")


if __name__ == "__main__":
    np.set_printoptions(precision=5, suppress=True)
    tasks = (task_01, task_02, task_03, task_04, task_05, task_06, task_07, task_08,
             task_09, task_10, task_11, task_12, task_13, task_14, task_15, task_16)
    for number, task in enumerate(tasks, start=1):
        print(f"\n{number}")
        task()

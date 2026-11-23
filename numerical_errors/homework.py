import math
import random
import sys
from decimal import Decimal, localcontext
from fractions import Fraction
from itertools import combinations
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


PAIRS = ((3.14, math.pi), (2.718, math.e), (9.8, 9.81), (0.333, 1 / 3))


def relative_error(approx, exact):
    if exact == 0:
        return float("inf")
    return abs(approx - exact) / abs(exact)


def sequential_sum(values):
    total = 0.0
    for value in values:
        total += value
    return total


def task_01():
    errors = []
    for i, (x, exact) in enumerate(PAIRS, 1):
        delta = abs(x - exact)
        percent = 100 * relative_error(x, exact)
        errors.append((i, delta, percent))
        print(f"{i}) Δ = |{x} − {exact:.12g}| ≈ {delta:.9g}, δ ≈ {percent:.8g}%")
    for column, title in ((1, "Δ"), (2, "δ")):
        print(title, "от лучшего к худшему:", *(r[0] for r in sorted(errors, key=lambda r: r[column])))
    print("Порядки различаются . Относительная погрешность учитывает масштаб точного значения .")


def task_02():
    print(f"Мост: Δ = 3 м = 3000 мм, δ = {100 * relative_error(1247, 1250):.2f}%")
    print(f"Болт: Δ = 0.3 мм, δ = {100 * relative_error(9.7, 10):.1f}%")
    print("В миллиметрах ошибка измерения моста больше . По доле от точного размера сильнее ошибка измерения болта .")


def task_03():
    for pair in PAIRS:
        print(*pair, "→", relative_error(*pair))
    print("relative_error(1, 0) =", relative_error(1, 0))
    print("Функция возвращает относительную ошибку в долях единицы . Для нулевого эталона она по условию возвращает inf .")


def task_04():
    x, r = 47.3, 0.001
    print("47.3 / 1.001 ≤ x* ≤ 47.3 / 0.999")
    print(f"Границы до восьми знаков: [{x / (1 + r):.8f}, {x / (1 - r):.8f}]")
    print("Из |47.3 − x*| ≤ 0.001 · |x*| следует, что точное значение положительно .")
    print("После раскрытия модуля получаем 0.999 · x* ≤ 47.3 ≤ 1.001 · x* .")


def task_05():
    limit = 0.3 / 0.005
    print(f"0.005 · |T| ≤ 0.3  ⇒  −{limit:g} °C ≤ T ≤ {limit:g} °C")
    print("Внутри интервала предельная абсолютная ошибка B меньше, а на границах пределы равны .")
    print("За пределами интервала меньшую максимальную ошибку гарантирует A .")


def task_06():
    for x, n, forms in (
        ("0.004520", "4", "4.520 × 10⁻³"),
        ("1200", "2–4", "1.2 / 1.20 / 1.200 × 10³"),
        ("1.200", "4", "1.200 × 10⁰"),
        ("10.03", "4", "1.003 × 10¹"),
        ("0.03050", "4", "3.050 × 10⁻²"),
        ("250000", "2–6", "2.5 / 2.50 / 2.500 / 2.5000 / 2.50000 × 10⁵"),
    ):
        print(f"{x:>8}   {n:>3}   {forms}")
    print("Начальные нули задают положение запятой, внутренние нули значащие .")
    print("У целого числа конечные нули могут обозначать как точность измерения, так и разряд .")


def task_07():
    print(f"{4.738291:.2f} ± 0.02")
    print("После округления до сотых остаются три значащие цифры .")
    print("Запись 4.738291 ± 0.02 приписывает результату лишнюю точность за пределами сотых .")


def task_08():
    print(*(round(x) for x in (0.5, 1.5, 2.5, 3.5, -0.5, -1.5, -2.5)))
    rng = random.Random(42)
    before = even = up = 0.0
    for _ in range(1_000_000):
        x = rng.randrange(10) + 0.5
        before += x
        even += round(x)
        up += math.floor(x + 0.5)
    print(f"Сдвиг вверх: {up-before:+g}, к чётному: {even-before:+g}, разность методов: {up-even:+g}")
    print("На точной половине round выбирает ближайшее чётное целое .")
    print("При равномерном выборе k ошибки округления к чётному в среднем компенсируются .")
    print("Округление вверх добавляет по 0.5 каждый раз, что за миллион операций завышает итог на 500 000 единиц .")


def task_09():
    terms = [1 / k for k in range(1, 101)]
    ref = math.fsum(terms)
    a = sequential_sum(terms)
    b = sequential_sum(round(x, 3) for x in terms)
    print(f"math.fsum = {ref:.17g}")
    for name, val in (("Без округления", a), ("До тысячных", b)):
        print(f"{name}: S = {val:.17g}, Δ = {abs(val-ref):.8g}, δ = {relative_error(val, ref):.8g}")
    if a == ref:
        print("Без округления сумма совпала с math.fsum, поэтому отношение ошибок не определено .")
    else:
        print(f"Промежуточное округление увеличило ошибку в {abs(b-ref)/abs(a-ref):.4g} раз .")
    print("Слагаемые следует сохранять с полной доступной точностью и округлять итог .")


def task_10():
    x = 0.1 + 0.2
    print(x, "   == 0.3:", x == 0.3, "   isclose:", math.isclose(x, 0.3))
    print(f"Δ = {abs(x-0.3):.8g}, δ = {relative_error(x, 0.3):.8g}")
    print("Одна десятая в двоичной записи превращается в бесконечную периодическую дробь .")
    print("В памяти помещается конечное число разрядов, поэтому сохраняется ближайшее представимое число .")
    print("После сложения результат оказывается рядом с сохранённым значением трёх десятых .")


def task_11():
    diff = (1 + 1e-15) - 1
    print(f"Ожидалось 1e-15, получено {diff:.17g}, δ = {relative_error(diff, 1e-15):.6%}")
    a, b, c = 1., 1e8, 1.
    root = math.sqrt(b*b - 4*a*c)
    direct = ((-b - root) / (2*a), (-b + root) / (2*a))
    q = -0.5 * (b + math.copysign(root, b))
    stable = (q/a, c/q)
    with localcontext() as ctx:
        ctx.prec = 80
        B = Decimal("1e8")
        ref = -2 / (B + (B*B - 4).sqrt())
        err1, err2 = (abs((Decimal.from_float(x) - ref) / ref) for x in (direct[1], stable[1]))
        print("Прямая формула:", direct, "   устойчивая:", stable)
        print(f"Малый по модулю корень: эталон {ref:.24g}, δ напрямую {err1:.5g}, δ устойчиво {err2:.5g}")
        print(f"Вычитание близких чисел усилило влияние ошибки округления .")
        print(f"Вычисление второго корня по произведению корней уменьшило его ошибку в {err1/err2:.4g} раз .")


def task_12():
    arr = [0.1] * 1_000_000
    print(f"{'Метод':<12} {'Сумма':>21} {'Δ':>13} {'δ':>13}")
    for name, method in (("Цикл", sequential_sum), ("sum", sum), ("math.fsum", math.fsum)):
        val = method(arr)
        print(f"{name:<12} {val:21.15f} {abs(val-1e5):13.6g} {relative_error(val, 1e5):13.6g}")
    print("У наивного цикла накапливается ошибка округления, а math.fsum даёт ровно 100000 .")
    print("Для метода с нулевой ошибкой конечное отношение погрешностей вычислить нельзя .")
    print("Результат встроенного sum зависит от версии Python .")


def task_13():
    small, big = [1e-10]*500_000, [1e6]*500_000
    ref = math.fsum(small + big)
    print("math.fsum =", ref)
    for name, data in (("Малые первыми", small + big), ("Большие первыми", big + small)):
        val = sequential_sum(data)
        print(f"{name}: {val!r}, Δ = {abs(val-ref):.9g}")
    print("Малые слагаемые успевают образовать заметную сумму, если сложить их первыми .")
    print("При обратном порядке каждое из них меньше половины шага между соседними float возле накопленной суммы .")


def task_14():
    factor = 1.0001
    log_factor = math.log(factor)
    errors = []
    x = 1.0
    for step in range(1, 10_001):
        x *= factor
        ref = math.exp(step * log_factor)
        errors.append(relative_error(x, ref))
    print(f"На шаге 10000: x = {x:.17g}, эталон = {ref:.17g}, δ = {errors[-1]:.5g}")
    for limit in (1e-9, 1e-6, 1e-3):
        first = next((i for i, err in enumerate(errors, 1) if err > limit), None)
        print(f"Порог {limit:g}: {first if first is not None else 'не превышен за 10000 шагов'}")
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(range(1, len(errors)+1), errors, linewidth=0.85)
    ax.set(xlabel="Номер шага", ylabel="Относительная погрешность", xlim=(1, len(errors)))
    ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(Path(__file__).with_name("error_growth.png"), dpi=150)
    plt.close(fig)
    print(f"Максимальная наблюдаемая относительная ошибка составила {max(errors):.3g} .")
    print("Ошибки отдельных умножений могут частично компенсироваться, поэтому рост немонотонный .")


def task_15():
    total = 0.0
    kopecks = 0
    with localcontext() as ctx:
        ctx.prec = 28
        amount = Decimal("0.00")
        cent = Decimal("0.01")
        for _ in range(1_000_000):
            total += 0.01
            amount += cent
            kopecks += 1
        diff = abs(Decimal.from_float(total) - amount)
        print("float:", repr(total), "рублей, Decimal:", amount, "рублей, int:", kopecks, "копеек")
        print(f"float − Decimal по модулю: {diff:.10g} рубля, {100 * diff/amount:.10g}%")
        print("Ошибка целых копеек:", abs(kopecks * cent - amount), "рубля")
    print("Точный итог начислений составляет 10 000 рублей, его дают Decimal и целые копейки .")
    print("В float одна копейка представляется приближённо, и повторные сложения накапливают расхождение .")


def task_16():
    rng = random.Random(42)
    values = [rng.random() for _ in range(100_000)]
    n = len(values)
    eps = Fraction.from_float(sys.float_info.epsilon)
    exact = sum(map(Fraction.from_float, values), Fraction()) / n
    means = {"Цикл": sequential_sum(values)/n, "sum": sum(values)/n,
             "math.fsum": math.fsum(values)/n, "numpy.mean": float(np.mean(values))}
    errors = {}
    for name, mean in means.items():
        errors[name] = abs(Fraction.from_float(mean) - exact) / eps
        print(f"{name:<10} {mean:.17g}   |ошибка|/ε = {float(errors[name]):.6g}")
    for a, b in combinations(means, 2):
        print(f"{a} / {b}: {abs(means[a]-means[b])/float(eps):.6g} ε")
    best = ", ".join(name for name, err in errors.items() if err == min(errors.values()))
    print(f"Ближе всего к точному рациональному среднему в этом запуске: {best} .")
    print("NumPy часто складывает значения попарно, что уменьшает потери при накоплении .")
    print("math.fsum отдельно учитывает частичные суммы, поэтому последние биты результатов могут различаться .")


if __name__ == "__main__":
    tasks = (task_01, task_02, task_03, task_04, task_05, task_06, task_07, task_08,
             task_09, task_10, task_11, task_12, task_13, task_14, task_15, task_16)
    for number, task in enumerate(tasks, 1):
        print(f"\n{number}")
        task()

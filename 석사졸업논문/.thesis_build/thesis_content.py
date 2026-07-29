from __future__ import annotations


def paragraphs(text: str) -> list[str]:
    return [block.strip().replace("\n", " ") for block in text.strip().split("\n\n") if block.strip()]


KOREAN_TITLE_LINES = [
    "극저온 3차원 낸드 플래시 메모리의",
    "시간 단계 독립형 물리 기반",
    "리텐션 손실 모델링",
]

ENGLISH_TITLE_LINES = [
    "Time-Step-Free Physics-Based",
    "Modeling of Retention Loss",
    "in Cryogenic 3-D NAND Flash",
]

KOREAN_ABSTRACT = paragraphs(
    """
    3차원 NAND Flash 메모리는 셀을 수직 방향으로 적층하여 높은 집적도를 확보하지만, 전하 트랩 기반 저장 구조에서는 시간에 따른 포획 전자의 방출이 문턱전압 분포를 변화시켜 리텐션 신뢰성을 제한한다. 특히 bandgap-engineered tunneling oxide(BE-TOX)와 charge trap nitride(CTN)에는 서로 다른 에너지와 위치를 갖는 트랩이 존재하므로, 단일 시정수나 경험적 감쇠식만으로는 소자 구조와 공정 변화가 리텐션 손실에 미치는 영향을 분리하기 어렵다. 다중 준위 저장과 극저온 응용이 확대될수록 물리적으로 해석 가능하면서 장시간 구간을 빠르게 예측할 수 있는 모델의 필요성이 커진다.

    본 논문은 먼저 김민수의 BE-TOX fast detrapping 분석을 출발점으로 삼아, 짧은 리텐션 구간에서 trap-to-band tunneling(TBT), direct tunneling(DT), Poole-Frenkel(PF) emission 및 thermal emission(TE)이 전하 손실 곡선에 미치는 영향을 정리한다. 해당 연구는 온도와 BE-TOX 내부 N1 층의 위치에 따라 지배적인 방출 경로가 TBT 또는 DT로 달라질 수 있음을 보였지만, TBT의 attempt-to-escape frequency를 피팅 파라미터로 두었다. 따라서 공정 변화와 실측 트랩 분포를 외삽하려면 시도 주파수를 미시적 트랩 상태와 전자 저장고의 상태 밀도로부터 직접 유도할 필요가 있다.

    이를 위해 본 연구에서는 국소 트랩과 Si 채널 전도대 사이의 band-trap transition을 Fermi golden rule로 기술하고, 비정질 Si-N 결합 길이에 대응하는 트랩 체적과 이방성 유효질량을 포함한 density of states를 결합하여 TBT attempt-to-escape frequency를 유도한다. 다층 장벽의 transmission coefficient는 WKB 근사로 계산하며, 최종 emission rate는 시도 주파수와 전달 계수의 곱으로 표현된다. 제안 모델은 1k, 10k, 50k program/erase cycle에서 추출된 이중 Gaussian 트랩 분포와 BE-TOX 내부 산화막 두께 변화에 대해 TCAD 결과를 재현한다.

    다음으로 모델의 적용 영역을 BE-TOX에서 CTN으로 확장한다. CTN을 반경 방향의 다수 charge node로 분할하고 각 shell의 전하 변화를 ΔQ_i로 표현한 뒤, cylindrical Poisson 방정식의 경계조건을 선형 행렬로 정리한다. 동일한 채널 전기장을 유지하는 조건과 Cramer 법칙을 사용하면 모든 전위 계수를 반복적으로 구하지 않고도 임의의 CTN 전하 분포가 만드는 ΔV_th를 하나의 determinant 계산으로 얻을 수 있다. 이 구성은 균일 전하 분포를 가정하던 기존 반해석 모델의 한계를 줄이고, 위치 및 에너지로 이산화된 초기 전하 분포를 직접 입력으로 사용할 수 있게 한다.

    Time-step-free 모델을 도입하기에 앞서 CTN 리텐션 계산에서 trap-assisted tunneling(TAT)을 제외하고 detrapping만 고려한 근거를 별도 분석하였다. 본 연구가 대상으로 하는 fresh-cell, cryogenic-emulation 조건에서는 thermally activated transition을 억제하여 CTN 포획 전자의 직접 방출 성분을 분리한다. 또한 연구정리 자료의 effective route count 분석에 따르면 CTN에서 채널로 방출되는 detrapping 경로의 통과 넓이는 원주 방향으로 연속적인 반면, CTN-TOX-채널의 TAT 경로는 원자 규모 트랩 단면과 유효 트랩 수에 의해 제한된다. 1k-50k cycling 조건을 반영한 비교에서도 TAT 성분은 CTN detrapping보다 현저히 작아, 본 모델의 보정 범위에서는 detrapping 중심의 축약이 타당하다. 다만 높은 cycling, 장시간, 고온 또는 높은 TOX trap density에서는 이 가정의 재검토가 필요하다.

    마지막으로 각 위치와 트랩 에너지에서의 포획 전자 수를 1차 autonomous ODE로 표현하고 그 closed-form 해를 사용하여 목표 리텐션 시간의 전하 분포와 ΔV_th를 직접 계산한다. 극저온 직접 TCAD의 수렴 한계를 보완하기 위해 온도를 83 K까지 낮춘 경우와 전자 capture cross-section을 10^-31 cm^2까지 감소시킨 경우의 극한 경향을 비교하여 cryogenic-like TCAD benchmark를 구성하였다. 제안 모델은 t_TOX=3-5 nm에서 TCAD transient를 재현하고, iterative refresh 대비 10^9 s 이후에도 약 3% 이내의 차이를 보였다. 평균 계산 시간은 transient TCAD의 27483 s에서 3.926 s로 감소하여 약 7000배의 속도 향상을 달성하였다.

    주요어 : 3차원 NAND Flash 메모리, 극저온 리텐션, attempt-to-escape frequency, trap-to-band tunneling, CTN detrapping, time-step-free 모델링
    """
)

ENGLISH_ABSTRACT = paragraphs(
    """
    Three-dimensional NAND Flash memory achieves high density by vertically stacking charge-trap cells, but the emission of trapped electrons gradually shifts the threshold-voltage distribution and limits retention reliability. Because bandgap-engineered tunneling oxide (BE-TOX) and charge-trap nitride (CTN) contain traps with different energies and radial locations, an empirical decay function alone cannot separate the effects of device geometry, trap profile, and emission pathway. This thesis develops a physics-based modeling chain that connects microscopic trap-to-band emission to a time-step-free prediction of cryogenic retention loss.

    The study begins with the fast-detrapping framework reported by Minsoo Kim, in which trap-to-band tunneling (TBT), direct tunneling (DT), Poole-Frenkel emission, recapture, and thermal emission are quantitatively separated. That work established that the dominant loss path can change with temperature and with the position of the nitride layer inside BE-TOX, while the attempt-to-escape frequency of TBT remained a fitted quantity. To remove this limitation, a band-trap transition model is constructed using Fermi's golden rule, a localized trap perturbation, the trap volume associated with the amorphous Si-N bond length, and an anisotropic density of states. The WKB transmission probability through the multilayer barrier is then combined with the physically derived attempt frequency to obtain the complete TBT emission rate.

    The model is validated against calibrated TCAD simulations for experimentally extracted double-Gaussian trap profiles corresponding to 1k, 10k, and 50k program/erase cycles. It reproduces the effects of threshold-voltage shift and inner-oxide thickness over the investigated range, while explaining why the attempt frequency increases with trap depth whereas the total emission rate can decrease because of the exponentially reduced transmission coefficient.

    The framework is subsequently extended from BE-TOX to an arbitrary radial charge distribution in the CTN. The CTN is discretized into cylindrical charge nodes, and the electrostatic boundary conditions are assembled into a linear system. By enforcing an equal channel-field condition and exploiting Cramer's rule, the threshold-voltage shift is obtained directly from the node charges without solving every potential coefficient. This charge-to-threshold relation provides the electrostatic backbone of the time-step-free model.

    Before constructing the final model, the exclusion of trap-assisted tunneling (TAT) is examined explicitly. Under the fresh-cell cryogenic-emulation conditions used for calibration, thermally activated transitions are suppressed to isolate CTN detrapping. In addition, an effective-route-count comparison shows that the continuous circumferential emission area available to CTN detrapping is much larger than the atomic-scale area associated with intermediate TOX traps. The cycling-dependent comparison in the supplied research deck confirms that the TAT-only contribution remains substantially smaller than CTN detrapping within the investigated range. This is a scoped approximation rather than a universal statement; TAT must be reconsidered for heavily cycled, high-temperature, long-time, or high-TOX-trap conditions.

    Finally, a first-order autonomous detrapping equation is solved in closed form for every radial and energy bin. The trapped-charge distribution and threshold-voltage loss at any target retention time are evaluated directly from the initially programmed state, eliminating sequential transient time stepping. A cryogenic-like TCAD benchmark is obtained by comparing the limiting trends of temperature reduction down to 83 K and electron capture-cross-section reduction down to 10^-31 cm^2. The proposed model reproduces the calibrated TCAD transients for tunneling-oxide thicknesses of 3-5 nm, differs from an iterative refresh calculation by only about 3% beyond 10^9 s, and reduces the average runtime from 27483 s to 3.926 s. These results establish a compact and interpretable route from trap physics to efficient short- and long-term retention prediction.

    Keywords: 3-D NAND Flash memory, cryogenic retention, attempt-to-escape frequency, trap-to-band tunneling, CTN detrapping, time-step-free modeling
    """
)


CHAPTERS = [
    {
        "title": "제 1 장 서    론",
        "sections": [
            {
                "title": "제 1 절 연구 배경",
                "paragraphs": paragraphs(
                    """
                    인공지능과 고성능 컴퓨팅의 확산은 저장 장치가 처리해야 하는 데이터의 규모와 보존 시간을 동시에 증가시키고 있다. NAND Flash 메모리는 비휘발성, 낮은 대기전력, 높은 집적도라는 장점으로 모바일 기기와 데이터 센터의 핵심 저장 매체가 되었다. 특히 3차원 구조는 평면 미세화에만 의존하지 않고 수직 방향으로 셀 수를 늘릴 수 있어 비트 비용을 낮추었다 [1], [2]. 그러나 셀당 저장 비트 수와 적층 수가 증가할수록 문턱전압 분포에 허용되는 여유는 좁아지고, 시간에 따른 작은 전하 변화도 판독 오류로 연결될 수 있다.

                    전하 트랩 기반 셀은 절연막 내부의 국소화된 상태에 전자를 저장한다. 프로그램 동작은 높은 게이트 전압을 이용하여 전자를 저장층으로 주입하고, 소거 동작은 반대 방향 전기장으로 전자를 제거한다. 저장 상태는 포획 전자의 총량과 공간 분포에 의해 결정되며, 이 두 정보는 채널 전기장과 문턱전압에 직접 반영된다. 따라서 리텐션 문제는 단순히 전자 수가 감소하는 현상이 아니라, 어떤 에너지와 위치의 전자가 어떤 경로로 이동하는가를 추적하는 문제이다.

                    3차원 원통형 구조에서는 채널, tunneling oxide, CTN, blocking oxide와 word line이 반경 방향으로 배치된다. 동일한 전하량이라도 채널에 가까운 위치와 word line에 가까운 위치가 만드는 전기적 결합은 서로 다르다. 또한 인접 word line과 공유되는 CTN 때문에 수평 방향 이동과 반경 방향 방출이 함께 나타날 수 있다. 그러므로 평면 구조에 맞춘 균일 전하 가정이나 단일 커패시턴스 근사는 최신 3차원 셀의 리텐션 해석에 충분하지 않다.

                    본 논문은 이러한 문제를 미시적 방출률, 반경 방향 전기장, 전하 분포의 시간 변화라는 세 층위로 분해한다. 먼저 BE-TOX의 fast detrapping을 통해 지배 경로를 파악하고, 이어서 TBT attempt-to-escape frequency를 물리적으로 유도한다. 그 결과를 CTN의 임의 전하 분포에 연결한 뒤 closed-form autonomous ODE를 사용하여 목표 시간의 문턱전압 손실을 직접 계산한다. 이 연속적인 구성은 정확도와 계산 효율을 동시에 확보하기 위한 것이다.
                    """
                ),
                "figures": [],
            },
            {
                "title": "제 2 절 리텐션 손실과 극저온 조건의 의미",
                "paragraphs": paragraphs(
                    """
                    리텐션 손실은 저장된 전자가 채널, word line 또는 다른 트랩으로 이동하면서 문턱전압이 변하는 현상이다. 단기 구간에서는 BE-TOX의 얕은 트랩에서 발생하는 fast detrapping이 중요할 수 있고, 장기 구간에서는 CTN detrapping, TAT, interface-trap recovery 및 lateral migration이 혼합될 수 있다 [5], [9]. 측정된 하나의 곡선은 여러 메커니즘의 합이므로, 물리 모델을 검증하려면 특정 성분이 우세한 조건을 선택하거나 각 경로의 제한 조건을 명확히 해야 한다.

                    극저온 실험은 열적으로 활성화되는 전이의 영향을 줄여 tunneling 기반 detrapping을 분리할 수 있다는 점에서 유용하다 [3], [4]. 그러나 4.2 K와 같은 조건을 TCAD에서 직접 재현하면 Fermi 통계, 포획과 방출, 비국소 터널링이 강하게 결합되어 수렴이 어려워질 수 있다. 본 연구는 직접적인 4.2 K 소자 전체 모사가 아니라, 측정의 시간 스케일에 맞춘 cryogenic-like benchmark를 사용한다. 따라서 결과는 절대적인 극저온 ΔV_th의 재현이 아니라 detrapping 중심 시간 의존성의 검증으로 해석해야 한다.

                    온도 독립적인 TBT가 지배적이면 최종 물리 시간이 길어져도 각 트랩의 방출 확률은 지수식으로 직접 계산할 수 있다. 반면 transient TCAD는 시작 시점부터 최종 시점까지 작은 time step을 순차적으로 적분하므로, 요구 리텐션 시간이 길수록 계산량이 증가한다. 이 차이는 장기 신뢰성 예측에서 결정적이다. 수년 규모의 목표 시간을 계산하기 위해 실제 시간축 전체를 따라갈 필요가 없다면, closed-form 해는 계산 구조 자체를 바꿀 수 있다.

                    다만 극저온이라는 이유만으로 모든 열적 성분이 완전히 사라진다고 단정할 수는 없다. 본 논문의 benchmark는 capture cross-section을 극한으로 감소시키는 수치적 조작과 온도 저하의 수렴 경향이 일치하는지를 확인하여 thermal transition 억제의 타당성을 점검한다. 동시에 비국소 터널링과 전기장 의존 장벽은 유지한다. 이처럼 제거되는 물리와 유지되는 물리를 분리하여 기술하는 것이 모델의 적용 범위를 판단하는 핵심이다.
                    """
                ),
                "figures": [],
            },
            {
                "title": "제 3 절 선행 연구와 연구의 출발점",
                "paragraphs": paragraphs(
                    """
                    김민수는 BE-TOX에서 발생하는 fast detrapping을 TBT, DT, PF emission, TE 및 recapture로 분리하고, 온도와 N1 위치에 따라 지배 경로가 달라짐을 보였다 [5]. 이 연구는 fast detrapping이 하나의 경험적 메커니즘이 아니라 여러 방출과 재포획 과정의 조합이라는 점을 정량화하였다. 특히 얇은 inner oxide에서는 TBT가 우세하고, N1이 CTN 쪽으로 이동하면 방출된 전도대 전자의 DT 성분이 상대적으로 중요해진다는 해석을 제공하였다.

                    그러나 기존 compact model에서 ν_TBT는 TCAD 결과에 맞추는 피팅 파라미터였다. 구조나 트랩 분포가 바뀌면 같은 값을 유지할 수 있다는 보장이 없고, 피팅 범위를 벗어난 외삽에는 물리적 근거가 약해진다. 또한 트랩 에너지 분포가 단일 준위가 아니라 shallow/deep Gaussian의 중첩으로 주어질 때, 각 준위의 상태 전이와 전자 저장고의 density of states가 시도 주파수에 어떻게 반영되는지 설명하기 어렵다. 이것이 attempt-to-escape frequency를 직접 유도해야 하는 첫 번째 동기이다.

                    Myung Jin과 Hyungcheol Shin의 연구는 국소 트랩 perturbation과 Si 채널 전도대의 상태를 연결하여 ν_TBT를 유도하고, WKB transmission coefficient와 곱하여 전체 emission rate를 구성하였다 [6]. 실측 기반 trap profile, ΔV_th, t_o1 변화에 대한 TCAD 비교는 피팅 시도 주파수 없이도 방출 transient를 설명할 수 있음을 보여 주었다. 이 단계는 트랩 에너지와 구조 변화가 시간 상수에 미치는 영향을 물리량으로 연결한다.

                    이후의 과제는 BE-TOX 한 층의 균일 분포를 넘어 CTN 내부의 임의 전하 분포를 다루는 것이다. Time-step-free 연구는 CTN을 반경 및 에너지 방향으로 이산화하고, 각 cell의 초기 전하와 방출률을 이용해 임의 시간의 분포를 직접 계산한다 [7]. 본 논문은 두 연구를 별개의 결과로 병렬 소개하지 않고, 첫 번째 연구가 제공한 미시적 방출률이 두 번째 연구의 autonomous ODE를 구성하는 방식으로 연결한다.
                    """
                ),
                "figures": [
                    (
                        "mj_ted_fig01_structure_and_reliability.png",
                        "3차원 NAND Flash 셀의 반경 방향 적층 구조, BE-TOX TBT 방출 및 문턱전압 분포 열화의 개념도 (출처: [6])",
                        "figure",
                    )
                ],
            },
            {
                "title": "제 4 절 연구 목표와 주요 기여",
                "paragraphs": paragraphs(
                    """
                    첫 번째 목표는 TBT emission rate에서 시도 주파수를 독립적인 피팅 상수가 아니라 트랩 에너지, 트랩 체적, 유효질량 및 전자 저장고 상태의 함수로 표현하는 것이다. 이를 위해 Fermi golden rule과 anisotropic density of states를 결합하고, Si-N 결합 길이로부터 국소 트랩 체적을 정의한다. 유도된 ν_TBT는 WKB 기반 |TC|와 분리되므로, 상태 전이의 빈도와 장벽 통과 확률이 각각 어떤 변수에 민감한지 해석할 수 있다.

                    두 번째 목표는 CTN의 비균일 전하 분포와 ΔV_th 사이의 전기적 관계를 계산 효율이 높은 형태로 정리하는 것이다. 반경 방향 shell의 charge node와 cylindrical capacitance를 사용하여 경계조건 행렬을 구성하고, Cramer 법칙으로 필요한 채널 전기장 조건만 추출한다. 이를 통해 전체 전위 계수를 매 시간 다시 구하지 않고도 문턱전압 변화를 계산한다.

                    세 번째 목표는 CTN 모델에서 TAT를 제외한 가정을 명시적으로 검증하는 것이다. 본 연구는 detrapping과 TAT를 동일한 이름의 전하 손실로 섞지 않고, 초기 상태, 중간 트랩의 필요성, 경로 단면적 및 cycling 의존성을 비교한다. 연구정리 PPT에 제시된 route count와 유효 trap 수를 이용하여 fresh-cell cryogenic-emulation 범위에서 detrapping이 우세한 이유를 설명하고, 가정이 깨질 수 있는 조건도 함께 제시한다.

                    네 번째 목표는 최종 물리 시간에 비례하지 않는 retention solver를 만드는 것이다. 각 반경/에너지 cell의 autonomous ODE를 closed form으로 풀고, 목표 시간 집합에 대해서만 전하 분포와 ΔV_th를 평가한다. TCAD, iterative refresh, 시간 단계 독립 계산을 같은 초기 조건에서 비교하여 정확도와 계산량의 절충을 정량화한다.
                    """
                ),
                "figures": [],
            },
            {
                "title": "제 5 절 논문의 구성",
                "paragraphs": paragraphs(
                    """
                    제 2 장에서는 3차원 NAND Flash의 전하 저장 구조와 리텐션 손실 메커니즘을 정리하고, 김민수의 fast detrapping 연구를 기반으로 TBT, DT, PF, TE 및 recapture의 역할을 분석한다. 온도와 N1 위치에 따른 지배 경로, stretched exponential parameter의 물리적 의미를 통해 이후 모델이 설명해야 할 관측량을 정의한다.

                    제 3 장에서는 attempt-to-escape frequency의 유도와 검증을 다룬다. 국소 트랩 Hamiltonian, Fermi golden rule, density of states, WKB 장벽 전달을 순서대로 전개하고, 실측 trap profile과 TCAD 비교로 모델의 구조/공정 민감도를 확인한다. 제 4 장은 CTN charge node와 Q-ΔV_th 관계를 유도하여 BE-TOX 모델을 전체 저장층으로 확장한다.

                    제 5 장은 Time-step-free 모델 이전에 필요한 범위 설정을 담당한다. CTN detrapping만을 autonomous ODE에 포함하고 TAT를 제외한 이유를 물리 경로와 유효 route count 관점에서 분석한다. 제 6 장에서는 cryogenic-like TCAD benchmark, closed-form ODE, t_TOX 변화, iterative refresh 및 계산 시간 비교를 통해 최종 모델을 검증한다. 제 7 장은 연구 결과와 제한 조건, 향후 확장 방향을 종합한다.
                    """
                ),
                "figures": [],
            },
        ],
    },
    {
        "title": "제 2 장 BE-TOX Fast Detrapping의 물리적 해석",
        "sections": [
            {
                "title": "제 1 절 3차원 전하 트랩 NAND Flash의 저장 구조",
                "paragraphs": paragraphs(
                    """
                    3차원 NAND Flash 셀은 원통형 poly-Si 채널 바깥쪽에 tunneling oxide, CTN, blocking oxide와 gate를 순서대로 배치한다. BE-TOX는 서로 다른 bandgap을 갖는 O1/N1/O2 적층을 사용하여 프로그램/소거 성능을 조절한다. 프로그램 전압이 인가되면 강한 전기장에 의해 전자가 채널에서 절연막을 통과하고, CTN뿐 아니라 BE-TOX의 N1 얕은 트랩에도 일부 전자가 포획될 수 있다 [5].

                    프로그램 종료 후 모든 단자 전압이 0 V로 돌아가면 전도대에 과도하게 축적된 전자는 빠르게 완화된다. 그러나 N1 또는 CTN 트랩에 남은 전자는 장벽을 넘어 채널이나 word line 방향으로 방출될 수 있다. BE-TOX에 비의도적으로 포획된 전자는 저장 데이터 자체를 담당하지 않지만, 방출되면서 프로그램 직후의 ΔV_th와 메모리 윈도우를 변화시킨다. 이것이 fast detrapping을 별도로 모델링해야 하는 이유이다.

                    전기적 결합은 반경 방향 위치에 따라 달라진다. 같은 전자 수라도 채널 가까이에 있는 트랩은 채널 전위와 강하게 결합하고, gate 가까이에 있는 전하는 다른 capacitance를 통해 문턱전압을 변화시킨다. 따라서 N1 층의 위치와 O1 두께는 단순한 터널링 거리뿐 아니라 초기 포획량, 전기장, 장벽 형태 및 ΔV_th 변환 계수를 동시에 바꾼다.

                    구조 해석에서는 각 층의 유전율과 반경, 균일 또는 비균일 전하 분포를 명시해야 한다. 김민수의 compact model은 BE-TOX의 N1과 CTN에 균일 전하를 가정하고 1차원 cylindrical Poisson 방정식을 풀어 O1과 N1의 평균 전기장을 구하였다 [5]. 본 논문은 이 해를 선행 기반으로 사용하되, 이후 CTN을 다수 shell로 나누어 비균일 분포를 허용한다.
                    """
                ),
                "figures": [
                    (
                        "km_fig01_betox_structure_and_paths.png",
                        "BE-TOX/CTN/BOX의 전하 분포와 fast detrapping 과정의 TBT, DT, PF 및 TE 경로 (출처: [5])",
                        "figure",
                    ),
                    (
                        "km_table01_model_parameters.png",
                        "BE-TOX fast detrapping 선행 모델에 사용된 구조 및 물리 파라미터 (출처: [5])",
                        "table",
                    ),
                ],
            },
            {
                "title": "제 2 절 프로그램 이후 포획 전자의 시간 변화",
                "paragraphs": paragraphs(
                    """
                    TCAD 프로그램 동작 직후 BE-TOX trap은 거의 채워진 상태로 나타난다. 리텐션 시간이 10^-4 s에서 10^-1 s로 증가하면 N1의 포획 전자 contour와 반경 분포가 빠르게 감소한다. 이 변화는 short-term retention의 시간 범위와 직접 겹치며, 단순한 장기 열화가 아니라 프로그램 직후부터 시작되는 빠른 전자 방출임을 보여 준다.

                    contour의 시간 변화를 모델에 사용하려면 방출과 재포획을 분리해야 한다. PF emission으로 N1 trap에서 전도대로 올라온 전자는 곧바로 채널로 빠져나가거나, 다시 비어 있는 trap에 포획될 수 있다. 반면 TBT는 trap에서 채널 전도대로 한 단계로 이동하므로 재포획 이전에 이미 charge-loss event가 완성된다. 이 경로 차이가 전체 곡선의 기울기와 β parameter에 반영된다.

                    포획 전자 분포는 위치뿐 아니라 에너지 축으로도 넓게 퍼져 있다. 얕은 trap은 상대적으로 빠르게 방출되고, 깊은 trap은 큰 시정수를 갖는다. 따라서 측정되는 stretched decay는 하나의 trap이 비정상적인 지수법칙을 따르기 때문이 아니라, 서로 다른 방출률을 가진 많은 trap의 합으로도 해석할 수 있다. 이후의 time-step-free 모델은 이 관점을 채택하여 각 energy bin에 독립적인 1차 방정식을 부여한다.

                    실험과 TCAD 사이의 역할도 구분할 필요가 있다. 실험은 실제 trap profile과 cycling 의존성을 제공하지만, 동시에 발생하는 경로를 완전히 분리하기 어렵다. TCAD는 특정 물리를 켜거나 끄는 방식으로 TE, DT, TBT의 기여를 순차적으로 보정할 수 있다. compact model은 그 결과를 구조 및 에너지 변수에 연결하여 더 넓은 조건을 빠르게 계산한다.
                    """
                ),
                "figures": [
                    (
                        "km_fig02_trapped_electron_contours.png",
                        "프로그램 직후부터 10^-1 s까지 BE-TOX 포획 전자 contour와 반경 분포의 변화 (출처: [5])",
                        "figure",
                    )
                ],
            },
            {
                "title": "제 3 절 방출 및 재포획 경로의 분해",
                "paragraphs": paragraphs(
                    """
                    N1의 얕은 trap에서 시작하는 첫 번째 경로는 TBT이다. 포획 전자는 O1과 N1 장벽을 양자 터널링하여 채널 전도대로 직접 이동한다. 방출률은 attempt-to-escape frequency와 장벽 transmission coefficient로 구성되며, 터널링 거리가 짧고 전기장이 강할수록 증가한다. 김민수 모델에서는 N1 내부의 분포 변화를 평균적으로 반영하기 위해 유효 터널링 거리에 대한 보정계수를 사용하였다.

                    두 번째 경로는 PF emission 후 DT 또는 TE로 이어지는 2단계 과정이다. 전기장은 Coulombic trap barrier를 낮추어 전자를 N1 전도대로 올리고, 전도대 전자는 O1을 직접 터널링하거나 열적으로 장벽을 넘는다. 동시에 capture rate는 전도대 전자를 다시 trap으로 되돌린다. 따라서 PF rate가 증가해도 실제 전하 손실은 DT/TE와 recapture의 경쟁에 의해 결정된다.

                    TE calibration은 높은 온도 범위에서 수행되었고, 추출된 attempt frequency는 3.0×10^5 s^-1이었다 [5]. ln(τ)와 1/k_BT의 기울기에서 얻은 activation energy는 약 1.28 eV로 E_t+ΔE_C와 비슷했다. 큰 유효 장벽과 긴 시정수 때문에 TE는 본 연구가 다루는 short-term retention 범위에서 거의 기여하지 않는다. 이 결과는 단지 rate가 작다는 수치적 관찰뿐 아니라 에너지 장벽의 크기로 설명된다.

                    DT calibration에서는 ν_DT=4.0×10^11 s^-1, 거리 보정계수 α'_DT=0.231 V^-1이 추출되었다 [5]. TBT calibration에서는 ν_TBT=4.2×10^6 s^-1, α'_TBT=0.537 V^-1이 사용되었다. 두 값의 차이는 시도 주파수만 비교해서 지배 경로를 판단할 수 없음을 보여 준다. 실제 emission은 시도 빈도와 장벽 통과 확률의 곱이며, 포획 전자의 초기 분포와 재포획도 함께 고려해야 한다.
                    """
                ),
                "figures": [
                    (
                        "km_fig03_thermal_emission_calibration.png",
                        "Thermal emission 보정 결과와 1.28 eV activation energy의 추출 (출처: [5])",
                        "figure",
                    ),
                    (
                        "km_fig05_dt_calibration.png",
                        "O1 두께와 온도 변화에 따른 DT 경로의 TCAD-model 보정 (출처: [5])",
                        "figure",
                    ),
                    (
                        "km_fig06_tbt_calibration.png",
                        "O1 두께와 온도 변화에 따른 TBT 경로의 TCAD-model 보정 (출처: [5])",
                        "figure",
                    ),
                ],
                "equations": [
                    "e_TBT = ν_TBT × |TC|",
                    "dn_t/dt = c_n n_c - (e_TBT + e_PF)n_t",
                    "dn_c/dt = e_PF n_t - (e_DT + e_TE + c_n)n_c",
                ],
            },
            {
                "title": "제 4 절 N1 위치와 초기 전하 분포",
                "paragraphs": paragraphs(
                    """
                    Bandgap engineering 공정에서 N1의 위치는 inner oxide O1 두께에 따라 이동한다. t_o1=1 nm일 때 장벽은 modified Fowler-Nordheim 형태를 이루며, N1의 일부는 포획 영역이고 일부는 터널링 영역이 된다. 포획 전자는 주로 N1의 바깥쪽 경계에 집중된다. 반대로 t_o1=3 nm에서는 삼각형 장벽이 형성되고 전자 분포가 N1 내부로 더 넓게 확장된다.

                    초기 ΔV_th는 t_o1=1 nm에서 2 nm로 증가할 때 BE-TOX 포획 전자 수가 증가하여 커진다. 2 nm 이후에는 전자 수 변화보다 capacitance 변화가 지배적이어서 ΔV_th가 소폭 감소한다 [5]. 이 비단조성은 두께 변화가 단순히 방출 시간만 바꾸는 것이 아니라 프로그램 직후 초기 조건과 전기적 결합까지 동시에 바꾼다는 점을 보여 준다.

                    따라서 리텐션 모델을 비교할 때 동일한 ΔV_th 또는 동일한 포획 전자 수를 무엇으로 고정했는지 명확히 해야 한다. 구조가 바뀌었는데 초기 분포를 동일하게 놓으면 실제 프로그램 동작의 차이가 빠지고, 프로그램을 다시 수행하면 방출 장벽 외에 초기 조건도 달라진다. 본 논문은 두 관점을 구분하여 모델 자체의 구조 민감도와 프로그램 이후 전체 transient를 각각 해석한다.

                    N1 위치 변화는 later time의 지배 경로에도 영향을 준다. 채널에 가까운 얇은 O1에서는 TBT transmission이 크고 1단계 방출이 우세하다. N1이 CTN 쪽으로 이동하면 TBT가 크게 감소하고 PF로 전도대에 올라온 전자의 DT가 중요해진다. 이 경로 전환은 activation energy와 stretched-exponential curve shape가 구조에 따라 달라지는 원인이다.
                    """
                ),
                "figures": [
                    (
                        "km_fig04_band_and_trapped_distribution.png",
                        "O1 두께에 따른 프로그램 band diagram, 포획 전자 분포 및 초기 ΔV_th 변화 (출처: [5])",
                        "figure",
                    )
                ],
            },
            {
                "title": "제 5 절 온도 및 위치에 따른 지배 경로",
                "paragraphs": paragraphs(
                    """
                    t_o1=2 nm에서 온도가 25°C, 65°C, 105°C로 증가하면 PF와 TE rate는 증가하지만 TBT와 DT의 기본 터널링 rate는 거의 유지된다. 그러나 전하 손실에 대한 실제 기여는 rate coefficient와 해당 상태의 carrier density를 곱한 density rate로 판단해야 한다. 25°C에서는 TBT가 주요 경로이며, 온도가 증가할수록 PF로 공급되는 전도대 전자와 DT의 기여가 커진다.

                    t_o1=1 nm에서는 TBT가 매우 강하여 105°C에서도 1단계 방출의 영향이 유지된다. PF로 올라온 전자 수가 증가해도 얇은 O1에서 recapture가 함께 커질 수 있으므로 PF coefficient만으로 총손실을 예측할 수 없다. 반대로 t_o1=3 nm에서는 TBT transmission이 크게 감소하여 넓은 온도 범위에서 DT가 지배적인 경로가 된다.

                    TE는 연구 온도 범위에서 전체 손실에 거의 영향을 주지 않는다. 이는 TE를 무조건 무시했다는 의미가 아니라, 고장 경로를 분리한 calibration에서 긴 시정수와 높은 activation energy가 확인되었다는 뜻이다. 모델의 적용 온도가 더 높아지거나 장벽이 달라지면 TE의 포함 여부를 다시 점검해야 한다.

                    이러한 결과는 지배 메커니즘을 하나의 고정된 레이블로 부르는 것이 위험함을 보여 준다. 'Fast detrapping'이라는 동일한 관측 곡선도 얇은 O1과 낮은 온도에서는 TBT가, 두꺼운 O1과 높은 온도에서는 PF-DT 연속 경로가 주도할 수 있다. 따라서 compact model의 파라미터는 물리 경로와 연결되어야 하며, 구조 변화에 따른 경로 전환을 보존해야 한다.
                    """
                ),
                "figures": [
                    (
                        "km_fig07_temperature_path_rates.png",
                        "t_o1=2 nm에서 온도에 따른 세부 방출률과 density rate 비교 (출처: [5])",
                        "figure",
                    ),
                    (
                        "km_fig08_position_path_rates.png",
                        "t_o1=1 nm와 3 nm에서 TBT, PF, DT 및 TE 기여의 비교 (출처: [5])",
                        "figure",
                    ),
                ],
            },
            {
                "title": "제 6 절 Stretched Exponential과 물리량의 연결",
                "paragraphs": paragraphs(
                    """
                    여러 trap energy와 위치를 합산한 리텐션 곡선은 stretched exponential function으로 잘 맞을 수 있다. ΔV_th(t)=ΔV_th,detrap[1-exp{-(t/τ)^β}]에서 τ는 대표 시간 척도이고 β는 곡선의 폭과 기울기를 나타낸다. 그러나 τ와 β는 그 자체로 방출 메커니즘이 아니며, 어떤 경로의 분포가 합쳐졌는지에 따라 다른 값을 갖는다.

                    N1이 채널 쪽으로 이동하여 TBT가 우세하면 1단계 방출의 비중이 커지고 β가 1에 가까워진다. O1이 두꺼워지면 PF 후 recapture가 개입하여 유효 손실 효율이 낮아지고, 서로 다른 시간 척도가 섞이면서 β가 감소한다. 김민수 연구는 β 변화가 TBT/PF 적분 비율과 PF/recapture 경쟁으로 설명될 수 있음을 보였다 [5].

                    ln(τ)와 1/k_BT의 기울기에서 얻은 activation energy도 지배 경로를 반영한다. t_o1가 작으면 온도 독립적인 TBT가 더 크게 기여하여 저온에서 기울기가 완만해진다. t_o1=3 nm처럼 TBT 비중이 낮은 경우에는 activation energy가 약 0.56 eV로 가장 크게 나타났다. 따라서 단일 activation energy를 전체 detrapping의 고정 물성으로 사용해서는 안 된다.

                    본 논문의 attempt-frequency 모델은 이러한 경험적 파라미터를 대체하기보다 그 기원을 설명하는 역할을 한다. 각 trap bin의 e_TBT를 물리적으로 계산하고 합산하면 stretched decay가 자연스럽게 형성되며, τ와 β는 결과를 요약하는 보조 지표가 된다. 이 접근은 trap profile이나 구조가 바뀌었을 때 새로운 τ와 β를 별도로 피팅하지 않고도 곡선을 예측할 수 있게 한다.
                    """
                ),
                "figures": [
                    (
                        "km_fig09_stretched_exponential_fit.png",
                        "N1 위치에 따른 detrapping 곡선과 stretched exponential fitting (출처: [5])",
                        "figure",
                    ),
                    (
                        "km_fig10_curve_shape_analysis.png",
                        "O1 두께에 따른 β_Detrapping 변화와 TBT-PF-recapture 경쟁의 해석 (출처: [5])",
                        "figure",
                    ),
                    (
                        "km_fig11_activation_energy.png",
                        "O1 두께별 ln(τ_Detrapping)과 activation energy 경향 (출처: [5])",
                        "figure",
                    ),
                ],
                "equations": [
                    "ΔV_th(t) = ΔV_th,detrap [1 - exp{-(t/τ_detrap)^β_detrap}]",
                ],
            },
        ],
    },
]

CHAPTERS.extend(
    [
        {
            "title": "제 3 장 Attempt-to-Escape Frequency의 물리 기반 모델링",
            "sections": [
                {
                    "title": "제 1 절 TCAD 구조와 초기 조건",
                    "paragraphs": paragraphs(
                        """
                        Attempt-to-escape frequency 모델의 검증에는 구조, 초기 전하 및 전기장이 일관된 TCAD 기준이 필요하다. 원통형 3차원 NAND string을 구성하고, 전체 word line에 동일한 프로그램 pulse를 인가하여 target cell과 주변 cell의 ΔV_th를 맞춘다. 프로그램 pulse 폭은 1 μs, rise/fall time은 각각 0.1 μs이며, 이후 모든 contact를 0 V로 설정하여 retention 동작을 수행한다 [6].

                        프로그램된 CTN 전하는 NAND string에 음의 gate bias와 유사한 효과를 주어 채널을 depletion 상태로 만든다. TCAD에서 target cell의 채널 전위는 대략 -ΔV_th에 해당하며, 이 전위는 BE-TOX trap과 채널 reservoir 사이의 barrier profile을 결정한다. 따라서 단일 셀의 수직 band diagram만 계산하는 것으로 충분하지 않고, string의 프로그램 상태가 제공하는 채널 경계조건을 포함해야 한다.

                        프로그램 과정에서는 강한 전기장으로 Fowler-Nordheim tunneling current가 형성되고 전도대 전자가 충분히 축적될 수 있다. retention에서는 V_G=0 V이고 Fermi level이 trap depth 부근으로 완화되어 전도대의 과도한 전자 축적이 억제된다. 이 차이 때문에 프로그램 시의 주입 경로와 retention 시의 방출 경로를 같은 식으로 취급할 수 없다.

                        초기 BE-TOX trapped-electron density는 의도된 데이터 저장 전하가 아니라 프로그램 중 형성된 부수적 전하이다. CTN 전하는 ΔV_th의 대부분을 만들지만, N1 전하는 빠른 시간 영역의 변화에 큰 영향을 줄 수 있다. 모델은 두 전하가 만드는 cylindrical Poisson 해를 사용하여 각 장벽의 전기장을 계산하고, N1의 시간 변화만 TBT ODE로 추적한다.

                        본 연구의 TCAD 비교는 모델의 미시적 파라미터를 무제한으로 피팅하기 위한 것이 아니다. 구조와 전하 분포를 먼저 보정하고, trap profile과 t_o1 및 ΔV_th를 독립적으로 변화시켜 예측성을 확인한다. 이 절차는 시도 주파수의 유도가 특정 한 조건에만 맞는 수치식이 아니라는 점을 검증한다.
                        """
                    ),
                    "figures": [
                        (
                            "mj_ted_fig02_tcad_program_retention.png",
                            "원통형 3차원 NAND string의 TCAD 설정과 프로그램/리텐션 band diagram의 차이 (출처: [6])",
                            "figure",
                        )
                    ],
                },
                {
                    "title": "제 2 절 지배적인 TBT 방출 가정",
                    "paragraphs": paragraphs(
                        """
                        BE-TOX detrapping에는 여러 경로가 가능하지만, retention bias에서 전도대 전자가 충분히 쌓이지 않으면 N1 전도대에서 채널로 이어지는 Fowler-Nordheim 또는 일반 direct tunneling은 제한된다. 반면 N1 trap과 채널 전도대 사이의 TBT는 포획 상태에서 전자 저장고로 직접 전이할 수 있다. 따라서 모델의 첫 단계에서는 dn_t,n1/dt를 -e_TBT n_t,n1으로 축약한다.

                        이 축약은 김민수 연구의 모든 조건을 부정하는 것이 아니다. 선행 연구에서 O1이 두껍거나 온도가 높을 때 PF-DT 경로가 중요해질 수 있음이 확인되었다 [5]. Attempt-frequency 모델의 검증 범위는 TBT가 우세하도록 설정된 retention 조건과 BE-TOX 구조이며, 온도 의존 thermal path는 별도 성분으로 남겨 둔다. 적용 조건을 벗어날 때에는 전체 rate equation을 다시 사용해야 한다.

                        TBT dominance는 이론적 방향성과 TCAD observation을 함께 사용한다. retention 상태에서 trap region의 Fermi potential이 채널보다 높으면 전자는 낮은 Fermi potential의 reservoir로 이동할 수 있다. 채널은 많은 연속 상태를 제공하며, 국소 trap은 제한된 공간의 perturbation으로 작용한다. 이 구성은 trap-to-band transition을 Fermi golden rule로 기술할 수 있는 물리적 기반이 된다.

                        방출률의 축약은 계산 효율에도 중요하다. 여러 경로가 비선형으로 carrier density를 교환하면 capture와 conduction-band population을 함께 적분해야 한다. TBT 단일 경로에서는 각 trap bin이 서로 독립인 1차 linear ODE가 되고, 일반해를 즉시 얻을 수 있다. 그러나 효율을 위해 물리를 제거한 것이 아니라, 지배 조건을 먼저 확인한 후 수학적 단순화를 적용했다는 순서가 중요하다.
                        """
                    ),
                    "figures": [],
                    "equations": [
                        "dn_t,n1/dt = -e_TBT n_t,n1",
                        "n_t,n1(t) = n_t0,n1 exp(-e_TBT t)",
                    ],
                },
                {
                    "title": "제 3 절 Band-Trap Transition의 상태 정의",
                    "paragraphs": paragraphs(
                        """
                        Band-trap transition model에서 초기 상태는 BE-TOX N1의 국소화된 trap이고, 최종 상태는 Si 채널 전도대의 연속 상태이다. 전이 방향은 두 영역의 Fermi level과 사용 가능한 최종 상태에 의해 정해진다. E_trap이 reservoir의 conduction-band edge E_C,r보다 높아야 탄성적인 trap-to-band 방출이 가능하며, E_trap이 더 낮은 경우에는 다른 열적 또는 다단계 메커니즘이 필요하다.

                        연속 trap energy profile은 수치 계산을 위해 energy bin i와 공간 bin j로 분할한다. 각 cell은 초기 전자 수 n_t0,i,j, trap energy, 위치, 채널 방향 장벽 및 word-line 방향 장벽을 가진다. 시간에 따른 전체 trapped charge는 모든 cell의 독립적인 지수 감쇠를 합한 값이다. 세분화 수가 증가할수록 원래 profile을 잘 보존하지만 계산량도 증가하므로 수렴 검사가 필요하다.

                        채널 전도대는 전자 reservoir로 모델링된다. 최종 상태의 점유 확률은 Fermi distribution f_r(E)로 나타나고, 방출 가능한 빈 상태의 비율은 1-f_r(E)이다. 본 조건에서는 E_trap이 E_C,r보다 충분히 높아 f_r(E_trap)≈0으로 근사되며, Pauli blocking의 영향이 작다. 이 근사는 reservoir 상태가 바뀌는 고농도 조건에서는 다시 평가해야 한다.

                        Trap-interface coupling은 국소 결함과 연속 band state 사이의 matrix element로 표현한다. 에너지 보존은 Dirac delta function으로 강제되고, trap depth와 trap volume이 transition strength를 결정한다. 이 구성은 단순 SRH prefactor와 달리 결함의 미시적 크기와 band의 state availability를 시도 주파수에 직접 포함한다.
                        """
                    ),
                    "figures": [
                        (
                            "mj_ted_fig03_band_trap_transition.png",
                            "Si 채널 reservoir와 BETOX trap 사이의 band-trap transition 및 다중 장벽 이산화 (출처: [6])",
                            "figure",
                        )
                    ],
                },
                {
                    "title": "제 4 절 WKB Transmission Coefficient",
                    "paragraphs": paragraphs(
                        """
                        시도 주파수가 trap에서 band로 전이하려는 빈도를 나타낸다면, transmission coefficient는 전자가 실제 다층 장벽을 통과할 확률을 나타낸다. BE-TOX에서는 O1과 N1이 서로 다른 유효질량, 유전율 및 장벽 높이를 갖기 때문에 단일 직사각형 barrier 근사보다 다중 trapezoidal barrier의 누적 효과가 중요하다.

                        각 barrier의 transmission은 WKB 근사로 계산하고 전체 |TC|는 barrier별 확률의 곱으로 구성한다. equivalent field F_eq는 해당 층 중심에서의 cylindrical electric field를 사용한다. 포획 전하와 CTN 전하가 바뀌면 Poisson 해를 통해 F_eq가 달라지고, 장벽의 높은 쪽과 낮은 쪽 에너지 Φ_H, Φ_L가 달라진다.

                        WKB exponent는 barrier height의 3/2승과 tunneling effective mass의 제곱근에 비례하고 electric field에 반비례한다. 따라서 산화막 두께가 0.5 nm만 변해도 전체 emission transient가 약 100배 달라질 수 있다 [6]. 이 민감도는 구조 공차가 리텐션 산포로 증폭될 수 있음을 의미한다.

                        WKB 근사는 전위가 원자 척도에서 급격히 변하지 않고 barrier가 충분히 완만하다는 조건에서 유효하다. 국소 trap 주변의 atomistic potential까지 직접 재현하지는 않지만, 장거리 절연막 barrier 통과를 compact하게 계산하는 데 적합하다. Trap 자체의 국소 전이는 별도의 Fermi golden rule 항에 포함하여 두 스케일을 분리한다.
                        """
                    ),
                    "figures": [],
                    "equations": [
                        "|TC| = Π_k exp[-(4√(2m*_k)/(3ħqF_eq,k))(Φ_H,k^1.5 - Φ_L,k^1.5)]",
                        "e_TBT = ν_TBT |TC|",
                    ],
                },
                {
                    "title": "제 5 절 Fermi Golden Rule 기반 시도 주파수 유도",
                    "paragraphs": paragraphs(
                        """
                        Attempt-to-escape frequency는 전이율 W(E), reservoir density of states D(E), 빈 최종 상태 비율 1-f_r(E)의 적분으로 정의한다. W(E)는 Fermi golden rule에 따라 localized perturbation Hamiltonian의 matrix element 제곱과 density of final state의 곱에 비례한다. 이 정의는 ν_TBT를 단순 진동 주파수나 경험적 상수로 두지 않고 실제 양자 상태 전이의 빈도로 해석하게 한다.

                        비정질 Si-N compound에서 over-coordinated 또는 under-coordinated atom이 electron/hole trap을 만들 수 있다는 선행 atomistic 결과를 사용한다 [17]. 평균 Si-N 결합 길이 1.7 Å를 trap의 선형 크기로 보고 V_T=(1.7 Å)^3의 국소 체적을 정의한다. Trap Hamiltonian은 V_T 내부에서 -|ΔE_T|, 외부에서 0인 perturbation으로 두어 trap depth와 공간적 크기를 동시에 반영한다.

                        Reservoir DOS는 tunneling 방향 유효질량 m*_n과 면내 유효질량 m_0를 분리한 anisotropic form을 사용한다. DOS는 √(E-E_C,r)에 비례하므로 trap level이 conduction-band edge보다 깊은 에너지 위치에 있을수록 사용 가능한 band state가 증가한다. 반면 WKB transmission은 barrier가 커지면서 지수적으로 감소한다. 두 항의 경쟁 때문에 ν_TBT는 trap depth와 함께 증가하더라도 전체 e_TBT는 감소할 수 있다.

                        E_trap≫E_C,r 조건에서 1-f_r≈1로 두고 적분하면 ν_TBT는 |ΔE_T|^2 V_T, 유효질량, √(E_trap-E_C,r)의 곱으로 정리된다. 이 식은 fitting-free라는 의미에서 모든 물성이 불확실하지 않다는 뜻은 아니다. Trap volume과 effective mass는 물리적으로 보정된 입력값이며, 그 불확실성은 결과의 sensitivity로 평가해야 한다. 중요한 점은 구조가 바뀔 때 임의의 ν를 다시 맞추지 않고 동일한 물리 규칙을 적용한다는 데 있다.

                        유도식은 BETOX TBT뿐 아니라 국소 trap과 연속 band reservoir가 연결되는 다른 trap-to-band scenario에도 적용할 수 있다. 다만 trap wave function이 넓게 비국소화되거나 phonon-assisted transition이 필수적인 경우에는 Hamiltonian과 energy-conservation 조건을 확장해야 한다. 본 논문의 사용 범위는 탄성적인 band-trap transition과 WKB barrier 통과가 지배적인 경우이다.
                        """
                    ),
                    "figures": [],
                    "equations": [
                        "ν_TBT = ∫ W(E)D(E)[1-f_r(E)]dE",
                        "W(E) = (2π/ħ)|ΔE_T|²V_T δ(E-E_trap)",
                        "ν_TBT = (2π/ħ)|ΔE_T|²V_T [m_0√(2m*_n)/(π²ħ³)]√(E_trap-E_C,r)",
                    ],
                },
                {
                    "title": "제 6 절 실측 Trap Profile의 이산화",
                    "paragraphs": paragraphs(
                        """
                        Endurance에 따라 BE-TOX trap density와 energy distribution은 달라진다. TSCIS로 추출된 profile은 bandgap 전체에 걸친 연속 분포이며, 1k, 10k, 50k P/E cycle에서 shallow와 deep peak의 위치 및 크기가 변화한다 [11]. 단일 trap level로 이 분포를 대체하면 특정 시간 범위만 맞고 곡선 폭과 cycling 의존성을 잃을 수 있다.

                        연속 profile은 두 개의 Gaussian component로 분해한다. 각 Gaussian은 평균 μ, 표준편차 σ, peak density를 가지며 shallow/deep trap population을 나타낸다. 수치 계산에서는 profile을 수백 개의 energy bin으로 나누고 각 bin에 농도, trap depth, ν_TBT, |TC|를 할당한다. 이 방식은 원래 profile의 면적과 주요 peak를 보존하면서 병렬 계산이 가능하다.

                        Trap profile과 장벽 구조는 서로 독립적으로 입력된다. 동일한 1k profile에 t_o1를 2-4 nm로 변화시키거나, 동일한 t_o1에서 cycling profile을 변경할 수 있다. 이 교차 비교는 모델이 단순히 하나의 TCAD curve를 재현한 것이 아니라 공정과 열화 변수를 분리해 예측하는지를 보여 준다.

                        이산화 오차는 bin 수를 늘리면 감소하지만, trap profile의 실험 불확실성보다 훨씬 작은 해상도를 사용하는 것은 계산 효율을 낭비할 수 있다. Time-step-free CTN 모델에서는 100 energy bin 이상에서 결과 변화가 작아지는 수렴 경향을 확인하였다 [7]. 따라서 실측 분포의 유효 해상도와 수치 수렴을 함께 고려하여 bin 수를 정한다.
                        """
                    ),
                    "figures": [
                        (
                            "mj_ted_fig04_trap_profile_and_specification.png",
                            "P/E cycle별 BETOX 실측 trap profile의 double-Gaussian fitting과 모델 파라미터화 (출처: [6], [11])",
                            "figure",
                        )
                    ],
                },
                {
                    "title": "제 7 절 TCAD 비교와 구조 변화 검증",
                    "paragraphs": paragraphs(
                        """
                        모델 검증은 ΔV_th=0-2 V, t_o1=2-4 nm, 1k/10k/50k trap profile을 조합하여 수행되었다 [6]. 초기 ΔV_th가 클수록 trapped electron이 만드는 electric field가 강해지고, 장벽 transmission이 증가하여 emission lifetime이 짧아진다. 이 경향은 TCAD scatter와 model line에서 일관되게 나타난다.

                        t_o1 변화는 가장 큰 구조 민감도를 보였다. 0.5 nm 차이만으로 transient가 약 두 자릿수 이동할 수 있으며, 전체 2-4 nm 범위에서 모델과 TCAD가 여러 cycling profile에 대해 일치하였다. 이 결과는 Poisson field와 WKB barrier가 구조 변화를 올바르게 전달하고 있음을 의미한다.

                        선행 모델은 ν_TBT를 fitting parameter로 사용하고 비선형 ODE를 수치적으로 풀었기 때문에 일부 조건에서 낮은 R²를 보였다. 물리적으로 유도된 ν_TBT와 linear ODE 일반해를 사용한 모델은 비교 표에서 R²≈0.99를 보였고, 선행 비교식은 음의 R²를 보였다 [6]. R² 하나만으로 물리 모델을 확정할 수는 없지만, 여러 구조 조건에서 동일한 parameter rule을 유지했다는 점이 중요하다.

                        계산 시간은 1 s 미만으로 보고되었다. 이는 TCAD의 비선형 반복을 energy/spatial bin별 독립 계산으로 치환하고 병렬화했기 때문이다. 그러나 빠른 계산은 초기 Poisson 해와 trap profile이 주어진다는 전제 위에 있다. 프로그램 동작 자체나 trap generation을 동시에 예측하는 문제는 별도의 모델 단계가 필요하다.
                        """
                    ),
                    "figures": [
                        (
                            "mj_ted_fig05_tcad_model_validation.png",
                            "ΔV_th, t_o1 및 cycling trap profile 변화에 대한 TCAD-model 검증 (출처: [6])",
                            "figure",
                        )
                    ],
                },
                {
                    "title": "제 8 절 ν_TBT와 전체 방출률의 해석",
                    "paragraphs": paragraphs(
                        """
                        유도된 ν_TBT는 trap level이 conduction-band edge에서 멀어질수록 대략 제곱 및 제곱근 항의 결합으로 증가한다. 깊은 trap은 localized perturbation의 에너지 차가 크고 reservoir에서 사용 가능한 state도 증가하기 때문이다. 그러나 이 증가만 보고 깊은 trap이 더 빠르게 방출된다고 결론 내릴 수 없다.

                        |TC|는 barrier height와 width에 지수적으로 민감하며, trap이 깊어질수록 빠르게 감소한다. 최종 e_TBT=ν_TBT|TC|에서는 transmission 감소가 우세하여 깊은 trap의 emission rate가 낮아진다. 이 곱셈 구조는 shallow/deep trap이 서로 다른 시간 영역을 지배하는 이유를 설명한다.

                        1k, 10k, 50k profile의 dominant shallow/deep 영역을 e_TBT curve에 투영하면 각 cycle의 대표 time constant를 예측할 수 있다. τ≈e^-1의 관계는 단일 bin의 1차 감쇠에서 직접 나오며, profile 전체의 stretched decay는 여러 τ의 중첩으로 형성된다. 따라서 cycle에 따른 곡선 이동을 trap density 증가뿐 아니라 energy peak 이동과 함께 해석할 수 있다.

                        본 장의 결과는 다음 장의 CTN 모델에 두 가지 입력을 제공한다. 첫째, 위치와 trap energy가 주어지면 채널 또는 word-line 방향 emission rate를 계산할 수 있다. 둘째, 각 bin의 시간 변화가 independent first-order ODE로 표현된다. 남은 과제는 변화한 전하 분포를 문턱전압으로 변환하는 electrostatic relation을 임의 CTN 분포에 대해 구성하는 것이다.
                        """
                    ),
                    "figures": [
                        (
                            "mj_ted_fig06_attempt_frequency_and_rate.png",
                            "Trap depth에 따른 ν_TBT, transmission coefficient 및 emission time constant의 관계 (출처: [6])",
                            "figure",
                        )
                    ],
                },
            ],
        },
        {
            "title": "제 4 장 CTN 전하 이산화와 Q-ΔVth 관계",
            "sections": [
                {
                    "title": "제 1 절 균일 전하 가정의 한계",
                    "paragraphs": paragraphs(
                        """
                        기존 cylindrical charge-trap transient 모델은 CTN 전체에 균일한 trapped charge density를 두는 경우가 많았다 [8]. 균일 가정은 closed-form Poisson 해를 단순화하지만, 실제 프로그램 이후의 전하 분포는 채널 및 word-line 경계, 프로그램 pulse, trap energy와 capture dynamics에 따라 비균일하다. 위치별 전하가 ΔV_th에 미치는 결합도 다르므로 총 전하만 같다고 동일한 문턱전압을 보장할 수 없다.

                        Time-step-free retention에서는 초기 분포가 핵심 입력이다. TCAD에서 추출한 post-program profile은 CTN의 한쪽 경계에 집중될 수 있으며, 각 trap energy도 서로 다른 위치 분포를 갖는다. 시간이 지나면 빠른 bin이 먼저 비워져 charge centroid가 이동한다. 따라서 모델은 임의의 radial profile을 보존하면서 전기장을 계산해야 한다.

                        CTN을 너무 세밀한 3차원 mesh로 직접 풀면 compact model의 장점이 줄어든다. 반면 하나의 uniform node는 중요한 공간 정보를 잃는다. 본 연구는 원통 대칭을 유지하면서 반경 방향을 N개의 shell로 나누는 절충을 사용한다. 각 shell의 전하는 node quantity로 표현되고, Poisson boundary condition은 N+2개의 선형 계수로 정리된다.

                        이산화의 목적은 TCAD mesh를 그대로 복제하는 것이 아니라 retention에 필요한 상태 변수를 최소화하는 것이다. Lateral migration을 명시적으로 풀지 않는 현재 범위에서는 radial coordinate와 trap energy가 주요 축이다. 향후 cell-to-cell 또는 word-line 방향 산포를 포함할 때는 axial index를 추가할 수 있지만, 본 장의 Q-ΔV_th relation은 각 axial slice에 공통적으로 적용할 수 있다.
                        """
                    ),
                    "figures": [],
                },
                {
                    "title": "제 2 절 Cylindrical Charge Node 구성",
                    "paragraphs": paragraphs(
                        """
                        CTN 반경 방향을 r_0부터 r_N까지 N개의 경계로 나누고, 각 구간의 trapped density를 n_t,i로 정의한다. 인접 구간의 density 차이는 경계에서의 equivalent node charge ΔQ_i=πr_i²(n_t,i-n_t,i-1)로 표현된다. 내부 density를 그대로 행렬에 넣는 대신 node charge를 사용하면 electric-displacement continuity와 자연스럽게 결합할 수 있다.

                        양 끝 경계에는 n_t,0=0과 n_t,N+1=0을 둔다. 이 조건은 CTN 바깥의 TOX와 BOX에 trapped charge density가 없다는 이산화 표현이다. 전체 CTN charge는 모든 ΔQ_i의 중첩으로 나타나며, 원통 shell의 실제 체적과 전자 전하 q를 곱해 물리적인 charge로 변환한다.

                        Node representation은 단순 그림상의 분할이 아니라 계산 그래프를 정의한다. 각 node는 양옆 cylindrical capacitance와 연결되고, TOX와 BOX는 채널 및 gate 경계로 연결된다. 초기 profile이 바뀌면 ΔQ vector만 바뀌고, 구조가 동일한 동안 capacitance matrix는 재사용할 수 있다. 이 재사용성이 많은 retention time과 cell variation을 계산할 때 효율을 높인다.

                        반경 분할 수 N은 정확도와 계산량을 결정한다. profile이 급격한 경계를 포함하면 적은 slice에서 centroid와 field가 부정확해질 수 있다. convergence test에서는 약 30 radial slice 이상에서 ΔV_th transient 변화가 작아졌다 [7]. 이후 계산은 30 slice를 기준으로 수행하되, 구조나 profile이 달라지면 다시 수렴을 확인한다.
                        """
                    ),
                    "figures": [
                        (
                            "mj_edl_fig01_charge_node_discretization.png",
                            "CTN의 반경 방향 전하 분포, cylindrical capacitance 및 equivalent charge node의 구성 (출처: [7])",
                            "figure",
                        )
                    ],
                    "equations": [
                        "ΔQ_i = πr_i²(n_t,i - n_t,i-1)",
                        "Q = Σ_i ΔQ_i",
                    ],
                },
                {
                    "title": "제 3 절 다층 Cylindrical Poisson 해",
                    "paragraphs": paragraphs(
                        """
                        TOX, N개의 CTN slice, BOX에서 전위는 cylindrical Poisson 방정식을 따른다. 전하가 없는 oxide에서는 V(r)=A ln r+B 형태이고, 균일 volume charge를 갖는 CTN slice에는 r² 항이 추가된다. 채널 경계의 V_ch와 gate 경계의 V_G를 Dirichlet condition으로 사용한다.

                        각 interface에서는 전위의 연속성과 transverse electric displacement εE의 연속성을 적용한다. N개의 CTN slice는 N-1개의 내부 interface를 만들고, TOX/CTN과 CTN/BOX 경계까지 포함하면 N+1개의 field-continuity equation이 얻어진다. 여기에 하나의 reference-potential condition을 더하여 N+2개의 미지 계수를 결정한다.

                        미지 vector x는 K_TOX, K_1,...,K_N,K_BOX로 구성한다. 계수 K는 각 층의 logarithmic potential과 electric field의 크기를 결정한다. Matrix A는 구조와 capacitance에 의해 결정되고, vector b는 node charge와 applied voltage condition을 포함한다. 동일한 구조에서는 A를 고정한 채 retention에 따라 b만 갱신할 수 있다.

                        시간 변화 중 Poisson 해를 매 step마다 완전히 다시 계산하는 것은 가능하지만 time-step-free 목적과 맞지 않는다. 본 연구는 initial field에서 emission rate를 계산하고, 목표 시간의 charge distribution을 closed form으로 얻은 뒤 Q-ΔV_th relation으로 전압을 변환한다. Field refresh의 영향을 확인하기 위해 별도의 iterative test를 수행하고 차이를 정량화한다.
                        """
                    ),
                    "figures": [
                        (
                            "mj_edl_fig02_band_initial_profile_parameters.png",
                            "채널과 word line 방향 barrier, 초기 CTN profile 및 cryogenic-emulation parameter deck (출처: [7])",
                            "figure",
                        )
                    ],
                    "equations": [
                        "V_TOX(r) = V_ch + (K_TOX/ε_TOX) ln(r/r_Si)",
                        "V_CTN,i(r) = V_CTN,i-1(r_i-1) + (K_i/ε_CTN) ln(r/r_i-1) + charge term",
                        "V_BOX(r) = V_CTN,N(r_N) + (K_BOX/ε_BOX) ln(r/r_N)",
                    ],
                },
                {
                    "title": "제 4 절 경계조건 행렬과 Capacitance 표현",
                    "paragraphs": paragraphs(
                        """
                        Electric-displacement continuity를 capacitance form으로 쓰면 A의 마지막 행에는 2π/C_TOX, 2π/C_i, 2π/C_BOX가 들어간다. 앞선 행들은 인접 K coefficient의 차이를 나타내는 1과 -1의 sparse structure를 갖는다. 이 구조는 N이 증가해도 규칙적으로 확장되며, dense 3차원 Poisson solver보다 메모리 요구가 작다.

                        Cylindrical capacitance는 길이와 유전율, 안쪽/바깥쪽 반경의 logarithmic ratio로 정의된다. 각 CTN slice의 폭이 작아질수록 C_i가 커지고 node charge가 만드는 국소 전위 변화가 세분화된다. Matrix의 conditioning은 slice 폭이 지나치게 불균일할 때 나빠질 수 있으므로, 기본 모델은 균일 radial partition을 사용한다.

                        Vector b의 앞부분은 ΔQ_i/2π, 마지막 성분은 ΔV=V_G-V_ch로 구성된다. 이 표현은 전하와 applied voltage의 선형 중첩을 명확히 한다. 임의 profile에 대한 결과는 각 node response의 합으로 볼 수 있고, 여러 cell profile을 계산할 때 matrix factorization 또는 determinant substructure를 재사용할 수 있다.

                        이 모델은 전하가 electric field를 바꾸는 electrostatic nonlinearity를 Poisson 방정식 자체에서는 선형으로 다룬다. 유전율과 geometry가 고정되고 charge density가 source term으로 들어가기 때문이다. 비선형성은 trap occupation과 emission rate가 field에 의존하는 결합에서 발생한다. Time-step-free approximation은 그 field dependence를 initial state에서 고정한다.
                        """
                    ),
                    "figures": [],
                    "equations": [
                        "A x = b",
                        "x = [K_TOX, K_1, ..., K_N, K_BOX]^T",
                        "b = [ΔQ_0/2π, ΔQ_1/2π, ..., ΔQ_N/2π, ΔV]^T",
                    ],
                },
                {
                    "title": "제 5 절 Cramer 법칙을 이용한 Q-ΔVth 계산",
                    "paragraphs": paragraphs(
                        """
                        문턱전압 변화는 동일한 채널 electric field를 유지하기 위해 gate voltage를 얼마나 바꾸어야 하는지로 정의할 수 있다. 채널 경계에서 F_TOX(r_Si)=K_TOX/(ε_TOX r_Si)이므로, 두 charge state의 K_TOX가 같아지는 gate-voltage difference가 ΔV_th이다. 따라서 x의 모든 coefficient를 구할 필요 없이 K_TOX 조건만 비교하면 된다.

                        Cramer 법칙에서 K_TOX는 b의 첫 번째 열을 대체한 determinant와 det(A)의 비로 나타난다. Charge가 없는 대신 ΔV_th를 인가한 경우와 node charge가 있지만 ΔV=0인 경우의 K_TOX를 같게 놓는다. Determinant의 multilinearity를 사용하면 det(A)와 여러 중간 coefficient가 소거되고, ΔV_th=-det[A_b(ΔQ_i,0)]의 단순한 관계를 얻는다 [7].

                        이 결과는 임의의 CTN profile에 대한 ΔV_th를 하나의 determinant computation으로 구할 수 있음을 뜻한다. 실제 구현에서는 구조가 고정된 A의 필요한 minor 또는 factorization을 미리 계산하여 반복 평가를 더 줄일 수 있다. 초기 profile, 목표 시간 profile 또는 Monte Carlo profile은 ΔQ vector만 바꾸어 동일한 변환을 사용한다.

                        Q-ΔV_th relation은 총 전하만 사용하는 capacitance model보다 charge centroid 정보를 보존한다. 채널 가까운 node의 전하가 감소하고 word-line 쪽 전하가 유지되면 총 전하 손실과 함께 결합계수도 달라진다. 이 효과는 radial distribution을 직접 입력하는 time-step-free 모델의 중요한 장점이다.

                        Determinant 식의 부호와 단위는 전자 charge의 정의, ΔV=V_G-V_ch convention, density-to-charge 변환에 따라 달라질 수 있다. 본 연구는 전자의 절대 전하 q를 양수로 두고 trapped electron density가 음의 source를 만든다는 convention을 일관되게 사용한다. 구현 검증에서는 uniform profile의 결과를 기존 analytic model과 비교하여 sign 및 scale을 확인한다.
                        """
                    ),
                    "figures": [],
                    "equations": [
                        "F_TOX(r_Si) = K_TOX/(ε_TOX r_Si)",
                        "K_TOX = det[A_b(ΔQ_i,ΔVth)]/det(A)",
                        "ΔV_th = -det[A_b(ΔQ_i,0)]",
                    ],
                },
                {
                    "title": "제 6 절 공간 및 에너지 이산화 수렴",
                    "paragraphs": paragraphs(
                        """
                        Time-step-free 결과의 정확도는 radial slice와 energy bin의 수에 좌우된다. Energy bin이 너무 적으면 shallow/deep peak의 면적과 tail을 정확히 표현하지 못하고, radial slice가 너무 적으면 채널 쪽 급격한 profile과 centroid 변화를 놓친다. 반대로 과도한 분할은 계산량을 증가시키고 실험 profile의 실제 해상도를 넘는 가짜 정밀도를 만든다.

                        Energy bin을 10-140개로 변화시킨 수치 실험에서 100개 이상부터 ΔV_th transient가 거의 수렴하였다. Radial slice를 5-50개로 변화시킨 경우에는 약 30개 이상에서 변화가 작아졌다. 이 결과를 기준으로 본 모델은 100 energy bin과 30 radial slice를 기본 설정으로 사용한다 [7].

                        수렴 기준은 최종 한 시점만이 아니라 전체 retention curve에 대해 평가해야 한다. 얕은 trap이 지배하는 초기 구간과 깊은 trap이 지배하는 장기 구간에서 필요한 energy resolution이 다를 수 있다. 따라서 log-spaced target time에서 최대 ΔV_th 차이와 curve shape를 함께 비교한다.

                        구조 변화나 다른 trap profile을 적용하면 기본 분할의 재검증이 필요하다. 예를 들어 t_TOX가 매우 얇아 field gradient가 커지거나, profile이 interface 근처에 좁게 집중되면 더 많은 radial slice가 필요할 수 있다. Compact model의 효율은 고정된 분할 수 자체가 아니라 요구 정확도에 맞는 최소 상태 수를 선택하는 데서 나온다.
                        """
                    ),
                    "figures": [],
                },
            ],
        },
    ]
)


CHAPTERS.extend(
    [
        {
            "title": "제 5 장 CTN 리텐션 모델에서 TAT 제외의 근거",
            "sections": [
                {
                    "title": "제 1 절 연구 질문과 모델의 적용 범위",
                    "paragraphs": paragraphs(
                        """
                        Time-step-free 모델을 구축하기 전에 먼저 답해야 할 질문은 CTN에서 빠져나오는 전하를 detrapping만으로 표현해도 되는가이다. 실제 3차원 NAND Flash에서는 CTN에 포획된 전자가 채널이나 word line로 직접 방출될 수 있고, tunneling oxide 내부의 중간 트랩을 경유하는 trap-assisted tunneling(TAT)도 가능하다. 두 경로를 구분하지 않으면 계산 속도를 높였더라도 모델이 어떤 물리 성분을 예측하는지 불명확해진다.

                        본 연구의 축약은 모든 동작 조건에서 TAT가 무시 가능하다는 주장이 아니다. 검증 대상은 fresh-cell 또는 낮은 열화 수준, thermal transition이 억제된 cryogenic-emulation 조건, 그리고 CTN detrapping 성분을 분리하도록 구성된 실험 및 TCAD이다. 이 범위에서는 CTN 포획 전자의 직접 방출이 관찰 곡선의 주된 성분이 되며, TAT는 유효 경로 수와 중간 트랩 점유 확률에 의해 제한된다.

                        경로 선택은 모델 파라미터에도 직접적인 영향을 준다. Detrapping 모델은 CTN 트랩 에너지, 공간 위치, 채널 및 word-line 방향 transmission coefficient를 사용한다. 반면 TAT를 포함하려면 TOX trap density, trap energy, capture cross-section, phonon-assisted transition, 두 단계 이상의 점유 상태와 전계 재분포를 추가해야 한다. 검증할 수 없는 파라미터를 한꺼번에 도입하면 동일한 리텐션 곡선을 여러 조합으로 맞출 수 있어 물리적 식별 가능성이 낮아진다.

                        따라서 본 장은 네 단계로 판단 근거를 정리한다. 첫째, CTN detrapping과 TAT의 물리적 경로를 분리한다. 둘째, 연구정리 자료의 면적 및 route-count 비교를 이용해 가능한 전이 경로 수를 정량화한다. 셋째, cycling에 따른 BETOX trap density를 반영한 TAT-only 계산과 CTN detrapping을 비교한다. 넷째, 극저온 측정과 TCAD가 thermal transition을 억제하여 모델 대상을 어떻게 분리하는지 검토한다.
                        """
                    ),
                    "figures": [],
                },
                {
                    "title": "제 2 절 CTN Detrapping과 Trap-Assisted Tunneling의 구분",
                    "paragraphs": paragraphs(
                        """
                        CTN detrapping은 CTN의 국소 트랩 상태에서 연속 상태인 채널 또는 word line로 전자가 방출되는 과정이다. 채널 방향 방출률 e_ch와 word-line 방향 방출률 e_WL은 각각의 장벽 높이, 전계, 유효 터널링 거리와 attempt-to-escape frequency에 의해 정해진다. 전자가 중간 상태에 머무르지 않는 직접 전이로 기술되므로, 초기 CTN 점유와 두 방향 방출률만 알면 1차 rate equation으로 표현할 수 있다.

                        TAT는 CTN과 채널 사이에 존재하는 TOX 트랩을 중간 상태로 사용한다. 최소한 CTN-to-TOX 전이와 TOX-to-channel 전이가 연속적으로 일어나야 하며, 중간 트랩이 비어 있어야 포획이 가능하고 다시 채널로 방출되어야 전체 전하 손실이 완성된다. 각 단계는 트랩 위치, 에너지, 전계와 phonon coupling에 의존하므로 하나의 transmission coefficient로 환원하기 어렵다.

                        두 과정은 온도 의존성에서도 차이가 난다. 직접 터널링 성분은 장벽과 파동함수 겹침의 영향을 크게 받으며 낮은 온도에서도 남을 수 있다. 반면 다중 단계 TAT의 포획과 방출에는 열적 활성화가 포함될 수 있고, 극저온에서 recapture와 phonon-assisted transition의 상대적 비중이 달라진다. 이 차이를 이용하면 온도를 낮추거나 capture cross-section을 감소시켜 thermal transition을 억제한 비교 조건을 만들 수 있다.

                        측정 곡선만으로 두 경로를 완전히 분리하기는 어렵다. 동일한 문턱전압 감소라도 다수의 느린 TAT 경로와 소수의 빠른 CTN detrapping 경로가 유사한 시간 의존성을 만들 수 있기 때문이다. 본 연구는 경로별 물리 파라미터를 독립적으로 추출하려는 대신, CTN detrapping이 지배적인 제한 조건을 먼저 설정하고 그 범위에서 time-step-free 해석의 정확성과 계산 속도를 검증한다.
                        """
                    ),
                    "figures": [],
                    "equations": [
                        "CTN detrapping:  n_t  →  channel 또는 word line",
                        "TAT:  CTN trap  →  TOX trap  →  channel",
                    ],
                },
                {
                    "title": "제 3 절 유효 방출 면적과 Route Count 비교",
                    "paragraphs": paragraphs(
                        """
                        연구정리 자료에서는 두 메커니즘이 사용할 수 있는 공간적 경로 수를 유효 면적으로 비교하였다. CTN detrapping은 word-line 길이 L_WL에 걸쳐 CTN과 TOX의 원주 방향 경계 전체에서 발생할 수 있다. 따라서 채널 방향으로 열려 있는 유효 면적은 원통 중심 반경 r_TOX,centroid를 사용하여 2πr_TOX,centroidL_WL로 근사할 수 있다.

                        TAT는 TOX 안에 실제로 존재하는 원자 규모 트랩을 통과해야 한다. 개별 트랩의 유효 단면을 a_trap²로 두면 전체 통과 면적은 N_trap,effa_trap²에 비례한다. 연구정리 자료는 비정질 Si-N 결합 길이에 해당하는 a_trap≈1.7 Å을 사용하였다. 연속 경계 면적을 사용하는 detrapping과 달리 TAT의 경로 수는 유효 트랩 개수에 의해 이산적으로 제한된다.

                        이 비교는 단순 면적비가 곧 emission-rate 비라는 뜻은 아니다. 각 경로의 장벽, attempt frequency, 점유 확률과 전계가 다르므로 최종 전류는 면적비 외의 물리량에도 의존한다. 다만 TAT가 가능한 위치의 수가 매우 적다는 사실은, 낮은 TOX trap density와 fresh-cell 조건에서 TAT 성분이 CTN 전체 경계에서 가능한 직접 방출을 압도하기 어렵다는 구조적 근거를 제공한다.

                        또한 route-count 관점은 cycling 의존성을 명확히 보여 준다. P/E cycling으로 BETOX trap density가 증가하면 N_trap,eff가 커지고 TAT 경로가 점차 늘어난다. 따라서 본 연구의 TAT 제외는 낮은 경로 수에 기반한 조건부 근사이며, 높은 cycling에서 동일한 결론을 자동으로 적용할 수 없다. 다음 절에서는 실제 cycling-dependent density를 사용한 정량 비교를 제시한다.
                        """
                    ),
                    "figures": [
                        (
                            "ppt_slide20_tat_route_count.png",
                            "CTN detrapping과 CTN-TOX-channel TAT의 유효 통과 면적 및 경로 수 비교 (출처: 연구정리 자료, 슬라이드 20)",
                            "figure",
                        )
                    ],
                    "equations": [
                        "A_detrapping = 2π r_TOX,centroid L_WL",
                        "A_TAT = N_trap,eff a_trap²,     a_trap ≈ 1.7 Å",
                    ],
                },
                {
                    "title": "제 4 절 Cycling-Dependent TAT의 정량 비교",
                    "paragraphs": paragraphs(
                        """
                        공급된 연구정리 자료는 1k, 10k, 50k P/E cycle에서 추출한 BETOX 총 trap density를 각각 4.49×10^16, 1.16×10^17, 1.89×10^17 cm^-3로 정리한다. 동일한 셀 체적과 유효 전이 영역을 적용하면 실제 TAT에 기여할 수 있는 유효 trap count는 각각 약 0.55, 1.42, 2.03개이다. 즉 낮은 cycling에서는 셀당 유효 중간 트랩이 한 개보다 작을 수 있으며, 50k cycle에서도 평균적으로 수 개 수준이다.

                        이 유효 개수는 연속적인 trap density를 사용하는 compact model과 실제 소자의 이산적 변동 사이의 차이도 암시한다. 평균 trap count가 1에 근접하면 셀마다 TAT 경로의 존재 여부가 달라질 수 있고, ensemble-average 곡선은 개별 셀의 거동을 그대로 나타내지 않는다. 본 논문은 평균적인 리텐션 손실을 대상으로 하므로 density 기반 비교를 사용하지만, 향후 tail-cell 예측에는 확률적 trap-count 모델이 필요하다.

                        동일 자료의 계산 결과에서 TAT-only ΔV_th 성분은 조사한 시간 구간과 cycling 범위에서 CTN detrapping 결과보다 현저히 작게 유지된다. Cycling 증가에 따라 TAT 성분이 커지는 경향은 확인되지만, fresh-cell cryogenic-emulation 모델의 보정 대상 곡선을 지배할 정도는 아니다. 이 결과는 route-count 논의와 일관되며, time-step-free 모델의 상태변수를 CTN 점유량으로 한정할 수 있는 정량적 근거가 된다.

                        다만 비교 결과의 세로축과 시간 스케일은 사용한 파라미터 deck에 의존한다. 특히 TOX trap energy와 capture cross-section이 달라지면 TAT의 절대 크기는 변할 수 있다. 따라서 본 연구는 TAT가 본질적으로 중요하지 않다고 결론 내리지 않고, 주어진 실험·TCAD 조건에서 TAT를 제외해도 검증 오차보다 작은 성분으로 남는다고 해석한다.
                        """
                    ),
                    "figures": [
                        (
                            "ppt_slide21_tat_quantitative_comparison.png",
                            "Cycling에 따른 BETOX trap density, 유효 trap count 및 TAT-only와 CTN detrapping의 정량 비교 (출처: 연구정리 자료, 슬라이드 21)",
                            "figure",
                        )
                    ],
                    "equations": [
                        "N_trap,eff = N_trap,total × V_effective",
                        "N_trap,eff(1k, 10k, 50k) ≈ 0.55, 1.42, 2.03",
                    ],
                },
                {
                    "title": "제 5 절 극저온 조건을 이용한 Detrapping 성분의 분리",
                    "paragraphs": paragraphs(
                        """
                        극저온 측정은 단순히 동작 온도를 낮추는 실험이 아니라, 여러 전하 이동 경로의 상대적 비중을 바꾸는 분리 도구로 사용된다. 온도가 낮아지면 thermal emission과 phonon-assisted capture가 억제되고, 장벽 투과에 의해 결정되는 detrapping 성분이 상대적으로 두드러진다. 연구정리 자료의 실험 구성은 이러한 thermal transition suppression을 이용하여 CTN detrapping 중심의 retention loss를 관찰한다.

                        실제 4.2 K에서 모든 TCAD 물리 모델이 안정적으로 수렴하는 것은 아니다. 낮은 온도에서는 Fermi 통계, incomplete ionization, 이동도와 접촉 조건이 강한 비선형성을 보이고, 긴 transient를 직접 계산할 때 수치적 강성이 커진다. 따라서 본 연구는 4.2 K 절대값을 그대로 재현했다고 주장하지 않고, 두 가지 독립적인 cryogenic-like 접근의 제한 경향을 비교한다.

                        첫 번째 접근은 온도를 83 K까지 감소시켜 열 활성화 전이를 물리적으로 줄인다. 두 번째 접근은 기준 온도에서 electron capture cross-section σ_n을 10^-16 cm²에서 10^-31 cm²까지 낮추어 recapture와 thermal transition의 효과를 수치적으로 억제한다. 두 방식이 유사한 limiting transient로 수렴하면, 남은 곡선을 CTN detrapping 중심의 benchmark로 사용할 수 있다.

                        이 비교는 극저온에서 TAT가 완전히 사라진다는 증명이 아니다. 다만 time-step-free 모델이 재현해야 할 대상 곡선이 thermal capture와 중간 트랩 전이를 최소화한 조건에서 생성되었음을 보인다. 따라서 모델 검증의 인과 관계는 ‘낮은 온도이므로 모든 TAT가 없다’가 아니라 ‘열적 성분을 억제한 두 독립적 조건이 같은 detrapping 제한 거동으로 접근한다’는 것이다.
                        """
                    ),
                    "figures": [
                        (
                            "ppt_slide16_cryogenic_measurement.png",
                            "Thermal transition suppression을 이용한 극저온 측정과 CTN detrapping 성분 분리의 개념 (출처: 연구정리 자료, 슬라이드 16)",
                            "figure",
                        )
                    ],
                },
                {
                    "title": "제 6 절 TAT 제외 가정의 타당성 경계",
                    "paragraphs": paragraphs(
                        """
                        이상의 분석으로부터 TAT 제외가 타당한 범위는 명확하게 한정된다. 첫째, CTN 포획 전자의 직접 방출을 관찰하도록 thermal transition이 억제되어야 한다. 둘째, TOX 중간 트랩 수가 적은 fresh-cell 또는 낮은 cycling 조건이어야 한다. 셋째, 모델을 보정한 시간 범위와 전계 범위에서 TAT-only 성분이 CTN detrapping보다 충분히 작아야 한다. 이 세 조건이 동시에 만족될 때 상태변수를 CTN 점유로 축약할 수 있다.

                        반대로 높은 P/E cycling에서는 BETOX와 TOX에 결함이 누적되어 TAT 경로 수가 증가한다 [9], [11]. 고온에서는 thermally activated capture와 emission이 회복되고, 장시간 구간에서는 작은 TAT rate도 누적되어 문턱전압 손실에 기여할 수 있다. 높은 프로그램 전압이나 얇은 TOX로 전계가 증가하는 경우에도 중간 트랩을 통한 전이가 강화될 수 있다.

                        이러한 조건에서는 CTN detrapping 식에 경험적인 보정계수를 곱하는 방식보다 TAT 상태를 명시적으로 추가해야 한다. 각 TOX trap bin에 대해 점유율을 정의하고 CTN-to-TOX, TOX-to-channel, 역방향 recapture rate를 결합하면 coupled autonomous ODE system을 만들 수 있다. 행렬 지수 또는 고유모드 분해를 적용하면 time-step-free 철학을 유지하면서 TAT까지 확장할 가능성이 있다.

                        본 논문의 결론은 그러므로 모델의 단순화와 물리적 범위가 함께 제시되어야 한다는 점이다. TAT를 제외한 이유는 계산 편의를 위한 임의 선택이 아니라, 유효 경로 수, cycling-dependent 정량 비교, 극저온 성분 분리라는 세 근거에 기반한다. 이후 장의 time-step-free 결과는 이 적용 범위 안에서 해석하며, 범위를 벗어나는 조건은 향후 연구 항목으로 명시한다.
                        """
                    ),
                    "figures": [],
                },
            ],
        },
        {
            "title": "제 6 장 Time-Step-Free Physics-Based Retention Model",
            "sections": [
                {
                    "title": "제 1 절 초기 전하 분포와 방출률의 정의",
                    "paragraphs": paragraphs(
                        """
                        Time-step-free 계산의 입력은 프로그램 직후 CTN의 위치·에너지별 포획 전자 분포 n_t(r,E,0)이다. 본 연구에서는 TCAD에서 얻은 초기 분포를 30개의 radial slice와 100개의 trap-energy bin으로 이산화한다. 각 bin은 동일한 전기장 안에서도 서로 다른 장벽 높이와 점유량을 가지므로, 총 전하만 사용하는 모델보다 리텐션 곡선의 빠른 구간과 느린 tail을 동시에 표현할 수 있다.

                        각 bin의 전자는 채널 방향과 word-line 방향의 두 경로로 방출될 수 있다. 채널 방향 rate e_ch는 CTN에서 TOX를 지나 채널 전도대로 이동하는 transmission coefficient를 포함하고, word-line 방향 rate e_WL은 blocking oxide 방향 장벽을 포함한다. 두 경로가 독립적인 first-order escape channel이면 총 방출률은 e_tot=e_ch+e_WL로 합산된다.

                        방출률 계산에는 초기 electrostatic solution에서 얻은 local field를 사용한다. 이 선택은 보유 전하가 감소하면서 field가 변하는 feedback을 무시하는 근사이다. 그러나 retention 구간에서 프로그램 전하의 일부만 빠져나가고 초기 전계가 지배적인 경우에는 rate 변화를 제한할 수 있다. 본 연구는 별도의 iterative refresh 계산으로 이 근사가 장시간에서 만드는 오차를 정량화한다.

                        초기 분포를 그대로 입력으로 사용하기 때문에 프로그램 조건이나 t_TOX 변화는 profile과 transmission coefficient 양쪽에 반영된다. 동일한 closed-form 식을 유지하면서도 서로 다른 구조와 프로그램 문턱전압을 계산할 수 있으며, 매 시간 단계에서 TCAD를 다시 수행할 필요가 없다. 이것이 empirical stretched-exponential fitting과 구별되는 핵심이다.
                        """
                    ),
                    "figures": [
                        (
                            "mj_edl_fig02_band_initial_profile_parameters.png",
                            "채널 및 word-line 방향 장벽, 초기 CTN 전하 분포와 time-step-free 계산 파라미터 (출처: [7])",
                            "figure",
                        )
                    ],
                    "equations": [
                        "e_tot(r,E) = e_ch(r,E) + e_WL(r,E)",
                        "n_t(r,E,0) = programmed CTN trap occupation",
                    ],
                },
                {
                    "title": "제 2 절 Autonomous Rate Equation과 Closed-Form 해",
                    "paragraphs": paragraphs(
                        """
                        중간 TAT 상태와 recapture를 제외한 적용 범위에서 각 bin의 점유는 다른 bin과 직접 결합되지 않는다. 따라서 위치 r_i와 에너지 E_j에 있는 포획 전자 수는 dn_t,ij/dt=-(e_ch,ij+e_WL,ij)n_t,ij의 1차 autonomous ODE를 따른다. 계수가 시간에 무관하므로 해는 초기값에 단일 지수 감쇠를 곱한 형태로 정확하게 얻어진다.

                        목표 시간 t_k에서의 점유는 n_t,ij(t_k)=n_t,ij(0)exp[-e_tot,ijt_k]이다. 계산은 t_k 이전의 시간 점유를 필요로 하지 않으며, 각 목표 시간이 독립적이다. 따라서 1 s, 10^3 s, 10^9 s를 계산할 때 중간의 모든 time step을 순차적으로 통과하지 않는다. 원하는 log-spaced 시간 배열에 대해 vectorized exponential을 한 번 평가하면 된다.

                        각 radial slice의 총 전하는 energy bin 점유를 적분하여 얻는다. 이어서 제 4 장의 density-to-node 변환으로 ΔQ_i(t)를 만들고, determinant 기반 Q-ΔV_th 관계를 적용하여 문턱전압을 계산한다. 초기값과 목표 시간의 차이를 취하면 retention loss ΔV_th,loss(t)=V_th(0)-V_th(t)가 된다.

                        Closed-form 해의 장점은 계산 속도뿐 아니라 수치적 안정성이다. 매우 작은 rate와 매우 큰 목표 시간이 함께 존재해도 명시적 시간 적분의 step-size 제한이 없다. 다만 exp(-e_tot t)의 지수가 매우 커질 때 underflow가 발생할 수 있으므로, 구현에서는 일정 임계값보다 큰 곱을 완전 방출로 처리한다. 이는 물리적으로도 해당 bin의 잔류 점유가 수치 정밀도보다 작다는 의미이다.
                        """
                    ),
                    "figures": [],
                    "equations": [
                        "dn_t,ij/dt = -(e_ch,ij + e_WL,ij)n_t,ij",
                        "n_t,ij(t) = n_t,ij(0) exp[-(e_ch,ij + e_WL,ij)t]",
                        "ΔV_th,loss(t) = V_th(0) - V_th(t)",
                    ],
                },
                {
                    "title": "제 3 절 목표 시간 직접 평가 알고리즘",
                    "paragraphs": paragraphs(
                        """
                        전체 알고리즘은 구조 전처리, 방출률 전처리, 목표 시간 평가의 세 단계로 나뉜다. 구조 전처리에서는 TOX·CTN·BOX 반경과 유전율로 cylindrical capacitance matrix를 구성하고, Q-ΔV_th 변환에 필요한 determinant 또는 factorization을 저장한다. 동일한 소자 구조에서는 이 단계가 한 번만 필요하다.

                        방출률 전처리에서는 각 radial-energy bin의 장벽과 WKB transmission coefficient를 계산한다. Attempt-to-escape frequency는 제 3 장에서 유도한 band-trap transition 모델 또는 검증된 emission deck을 사용한다. 채널과 word-line 방향의 결과를 합산하여 e_tot 행렬을 만든다. 구조와 초기 bias가 동일하면 여러 목표 시간 계산에서 이 행렬을 재사용할 수 있다.

                        목표 시간 평가 단계에서는 t vector를 e_tot tensor와 broadcast하여 잔류 점유를 직접 계산한다. Energy 방향 적분, radial node charge 변환, Q-ΔV_th 계산을 연속적으로 수행하면 전체 retention curve를 얻는다. 시간 배열의 원소 수가 늘어날 때 계산량은 선형적으로 증가하지만, 최대 시간의 크기와는 무관하다. 10^3 s에서 10^12 s로 범위를 늘려도 time-step count가 폭증하지 않는다.

                        이 구조는 parameter sweep과 통계 분석에 특히 유리하다. t_TOX, 초기 ΔV_th, trap profile 또는 온도를 바꾼 수천 개의 case를 독립적으로 계산할 수 있고, 각 case의 목표 시간도 병렬화할 수 있다. 반면 transient TCAD는 앞선 시간의 수렴 결과가 다음 step의 초기값이므로 순차성이 강하고, 극저온처럼 stiff한 조건에서 계산 비용이 급격히 증가한다.
                        """
                    ),
                    "figures": [],
                    "equations": [
                        "Input → {geometry, n_t(r,E,0), e_ch(r,E), e_WL(r,E), target times}",
                        "Output → {n_t(r,E,t), Q_i(t), ΔV_th(t)}",
                    ],
                },
                {
                    "title": "제 4 절 Cryogenic-Like TCAD Benchmark의 구성",
                    "paragraphs": paragraphs(
                        """
                        직접적인 4.2 K transient TCAD는 수렴성과 모델 파라미터의 유효성 때문에 benchmark로 사용하기 어렵다. 연구정리 자료에서는 온도를 단계적으로 83 K까지 낮춘 simulation과 electron capture cross-section을 10^-31 cm²까지 줄인 simulation을 비교하였다. 두 조건은 서로 다른 방식으로 thermal transition과 recapture를 억제한다.

                        온도 감소 방식은 물리적 cryogenic trend를 직접 반영하지만, 매우 낮은 온도에서 semiconductor transport model이 불안정할 수 있다. Capture cross-section 감소 방식은 수치 수렴을 유지하면서 CTN으로 되돌아오는 전자를 억제하지만, 실제 온도를 나타내는 것은 아니다. 그러므로 두 결과가 같은 제한 곡선으로 접근하는지를 확인하는 것이 중요하다.

                        비교 결과, 온도 감소와 σ_n 감소에서 얻은 retention transient는 thermal component가 충분히 억제되면 유사한 경향으로 수렴한다. 본 연구는 이 limiting curve를 cryogenic-like TCAD로 정의한다. 이는 4.2 K의 절대 시간 상수를 정확하게 예측하는 표준이 아니라, detrapping 지배 조건에서 모델의 곡선 형태와 구조 의존성을 검증하는 상대 benchmark이다.

                        실험 ΔV_th는 arbitrary unit로 정규화된 부분이 있어 절대 시간 축 보정에는 한계가 있다. 따라서 측정은 모델의 온도 경향과 곡선 형태를 지지하고, TCAD는 t_TOX와 초기 profile 변화에 대한 내부 일관성을 제공한다. 두 자료의 역할을 구분하면 과도한 외삽을 피하면서 time-step-free 모델을 검증할 수 있다.
                        """
                    ),
                    "figures": [
                        (
                            "ppt_slide17_cryogenic_tcad_convergence.png",
                            "온도 감소와 electron capture cross-section 감소를 이용한 cryogenic-like TCAD 제한 곡선의 구성 (출처: 연구정리 자료, 슬라이드 17)",
                            "figure",
                        )
                    ],
                },
                {
                    "title": "제 5 절 구조 변화 및 실험 경향에 대한 검증",
                    "paragraphs": paragraphs(
                        """
                        제안 모델은 프로그램 ΔV_th=1.8 V의 초기 조건에서 t_TOX=3, 4, 5 nm 구조를 비교하였다 [7]. TOX가 두꺼워지면 채널 방향 장벽 폭이 증가하고 transmission coefficient가 감소하므로 retention loss가 느려진다. 이 구조 의존성은 단순 time-scale fitting이 아니라 각 radial bin의 WKB transmission을 통해 계산된다.

                        Time-step-free 결과는 조사한 t_TOX 범위에서 cryogenic-like TCAD transient를 재현한다. 초기 빠른 감소와 장시간 tail의 상대적 크기가 함께 유지되며, 하나의 공통 모델 구조로 여러 oxide thickness를 설명한다. 이는 임의의 stretched-exponential 파라미터를 구조마다 다시 피팅하는 방식보다 물리적 외삽 가능성이 높음을 의미한다.

                        극저온 측정과의 비교에서는 절대 ΔV_th보다 온도 저하에 따른 retention-loss 억제와 곡선 형태를 중심으로 평가한다. 측정의 세로축이 arbitrary unit이고 소자별 trap profile이 완전히 공개되지 않았기 때문에, 하나의 scale factor로 시간 축을 맞춘 뒤 상대적인 경향을 비교한다. 이 제한은 결과 해석과 향후 실험 설계에서 명시되어야 한다.

                        검증 범위는 fresh cell과 CTN detrapping이 지배적인 조건으로 한정된다. Bandgap-engineered 공정 변화나 높은 cycling으로 TOX trap이 증가한 경우에는 초기 profile과 경로 구성이 달라질 수 있다. 따라서 현재 결과는 특정 구조의 절대 수명 보증보다는, cryogenic retention을 빠르게 비교하는 physics-based compact framework로 해석하는 것이 타당하다.
                        """
                    ),
                    "figures": [
                        (
                            "ppt_slide18_cryogenic_model_validation.png",
                            "실험, cryogenic-like TCAD와 time-step-free 모델의 비교 및 t_TOX 의존성 검증 (출처: 연구정리 자료, 슬라이드 18)",
                            "figure",
                        )
                    ],
                },
                {
                    "title": "제 6 절 Iterative Field Refresh와 근사 오차",
                    "paragraphs": paragraphs(
                        """
                        Closed-form 모델은 초기 전계에서 계산한 방출률을 시간 전체에 사용한다. 전하가 빠져나가면 CTN과 TOX의 전위 분포가 변하고 transmission coefficient도 달라질 수 있으므로, 이 근사를 검증하기 위해 iterative field-refresh 계산을 수행하였다. Refresh 방법은 일정한 시간 구간마다 잔류 전하로 Poisson 해를 갱신하고 새로운 emission rate를 계산한다.

                        Iterative 결과는 전하-전계 feedback을 더 충실히 포함하지만, 다시 시간 순차 계산이 필요하다. 따라서 본 연구에서는 이를 최종 모델이 아니라 정확도 평가용 reference로 사용한다. 동일한 초기 profile과 target time을 적용하여 완전한 closed-form 결과와 비교하면, time-step-free 근사가 어느 구간에서 누적 오차를 만드는지 확인할 수 있다.

                        비교 결과 10^9 s 이후의 장시간 영역에서도 두 결과의 차이는 약 3% 수준에 머물렀다 [7]. 초기 전하 감소가 전체 프로그램 전하에 비해 제한적이고, 방출되는 성분이 주로 특정 에너지·위치의 bin에 집중되어 있어 전체 전계 변화가 크지 않기 때문이다. 이 오차는 transient TCAD의 파라미터 불확실성과 측정 분산보다 작은 수준이다.

                        그러나 더 큰 초기 ΔV_th, 매우 얇은 TOX 또는 장시간 동안 대량의 전하가 방출되는 조건에서는 refresh 오차가 증가할 수 있다. 실용적인 확장 방법은 목표 시간 구간을 몇 개의 큰 interval로 나누어 각 interval 시작점에서만 rate를 갱신하는 것이다. 이는 수천 개 time step을 사용하는 transient보다 훨씬 빠르면서 전계 feedback을 부분적으로 회복할 수 있다.
                        """
                    ),
                    "figures": [
                        (
                            "mj_edl_fig03_validation.png",
                            "Time-step-free 해와 iterative field-refresh 계산의 장시간 비교 및 cryogenic-like TCAD 검증 (출처: [7])",
                            "figure",
                        )
                    ],
                },
                {
                    "title": "제 7 절 계산 시간과 Computational Impact",
                    "paragraphs": paragraphs(
                        """
                        동일한 계산 환경에서 transient TCAD의 평균 실행 시간은 27483 s이고 time-step-free 모델은 3.926 s였다. 두 값을 나누면 약 7000배의 속도 향상에 해당한다. TCAD 시간은 nonlinear Poisson 및 carrier continuity 방정식을 다수의 time step에서 반복적으로 수렴시키는 비용을 포함하고, 제안 모델은 전처리된 rate와 행렬을 사용하여 목표 시간의 지수함수를 직접 평가한다.

                        속도 향상은 최대 retention time이 길어질수록 더 중요해진다. 산업적으로 요구되는 보존 시간은 10년 규모이지만, 이 시간을 직접 transient로 따라가려면 초기 빠른 변화와 후기 느린 변화를 모두 안정적으로 해석해야 한다. Time-step-free 방식에서는 10년을 나타내는 하나의 target time도 다른 시간점과 동일한 비용으로 계산된다.

                        빠른 실행은 단일 곡선보다 설계 공간 탐색에서 더 큰 가치를 갖는다. Oxide thickness, trap energy distribution, 프로그램 상태와 온도 조합을 수천 번 평가할 수 있고, sensitivity analysis를 통해 어떤 공정 파라미터가 장기 loss를 지배하는지 확인할 수 있다. 또한 compact model 형태이므로 array-level error model이나 controller-level lifetime simulation과 연결하기 쉽다.

                        계산 시간 비교는 사용한 mesh, solver tolerance와 하드웨어에 따라 달라지므로 7000배라는 수치를 보편적인 상수로 해석해서는 안 된다. 중요한 점은 sequential time stepping을 제거하여 비용의 scaling law를 바꿨다는 것이다. 목표 시간의 크기 대신 평가하는 radial-energy bin과 case 수가 계산량을 결정하며, 이 구조가 cryogenic long-term retention 분석의 병목을 완화한다.
                        """
                    ),
                    "figures": [
                        (
                            "ppt_slide19_computational_impact.png",
                            "Transient TCAD와 time-step-free 모델의 실행 시간 및 장시간 리텐션 계산 효율 비교 (출처: 연구정리 자료, 슬라이드 19)",
                            "figure",
                        ),
                        (
                            "mj_edl_table01_runtime_comparison.png",
                            "Transient TCAD와 제안 모델의 평균 계산 시간 비교 (출처: [7])",
                            "table",
                        ),
                    ],
                    "equations": [
                        "Speed-up = 27483 s / 3.926 s ≈ 7.0×10³",
                    ],
                },
                {
                    "title": "제 8 절 모델의 한계와 확장 방향",
                    "paragraphs": paragraphs(
                        """
                        첫 번째 한계는 초기 전계에서 emission rate를 고정하는 것이다. 현재 검증 범위에서는 약 3% 오차로 유지되지만, 큰 전하 손실이나 강한 field redistribution에서는 adaptive refresh가 필요하다. 두 번째 한계는 TAT와 recapture를 제외한 것이다. 제 5 장의 타당성 조건을 벗어나는 cycling·온도·시간 범위에서는 TOX trap 점유를 상태변수로 추가해야 한다.

                        세 번째 한계는 반경 방향 중심의 전하 분포이다. 실제 3차원 NAND string에서는 인접 word line 사이의 lateral migration과 fringing field가 장시간 retention에 영향을 줄 수 있다. Axial coordinate를 추가하면 상태 수가 증가하지만, 각 slice의 cylindrical Q-ΔV_th 변환을 block matrix로 확장하여 동일한 해석 철학을 유지할 수 있다.

                        네 번째 한계는 극저온 benchmark의 절대성이다. 83 K까지의 수렴 결과와 σ_n 감소 결과가 같은 limiting trend를 보이지만, 이는 4.2 K에서의 모든 scattering과 contact physics를 재현한 것은 아니다. 절대 시간 축을 확정하려면 trap-resolved spectroscopy, 다양한 program level, 여러 온도와 장시간 측정이 함께 필요하다.

                        향후에는 물리 기반 attempt frequency, CTN node model과 coupled trap network를 하나의 parameter-extraction workflow로 통합할 수 있다. 실측 분포에서 trap energy와 위치를 추출하고, uncertainty propagation으로 cell-to-cell retention tail을 예측하면 본 모델은 단일 평균 곡선을 넘어 신뢰성 설계 도구로 확장될 수 있다.
                        """
                    ),
                    "figures": [],
                },
            ],
        },
        {
            "title": "제 7 장 결    론",
            "sections": [
                {
                    "title": "제 1 절 연구 결과의 통합",
                    "paragraphs": paragraphs(
                        """
                        본 논문은 BE-TOX의 fast detrapping 분석에서 출발하여 CTN의 time-step-free retention 모델까지 이어지는 물리 기반 모델링 체계를 구축하였다. 김민수의 연구를 통해 TBT, DT, PF 및 TE 경로가 온도와 N1 위치에 따라 교차하는 조건을 정리하고, 기존 compact model에서 피팅 파라미터로 남아 있던 TBT attempt-to-escape frequency를 해결해야 할 핵심 문제로 정의하였다.

                        Fermi golden rule, 국소 트랩 체적, 이방성 density of states와 WKB transmission을 결합하여 attempt frequency와 emission rate를 분리하였다. 제안식은 1k, 10k, 50k cycling에서 얻은 이중 Gaussian 트랩 분포와 ΔV_th 및 t_o1 변화에 대한 TCAD 결과를 일관되게 재현하였다. Attempt frequency는 깊은 트랩에서 증가할 수 있지만 transmission coefficient의 지수 감소 때문에 전체 방출률은 오히려 작아진다는 점을 물리적으로 설명하였다.

                        CTN에서는 임의의 반경 방향 전하 분포를 cylindrical charge node로 변환하고, Poisson 경계조건과 Cramer 법칙으로 Q-ΔV_th 관계를 구성하였다. 이 electrostatic backbone에 위치·에너지별 autonomous detrapping equation의 closed-form 해를 결합하여 목표 시간의 전하 분포와 문턱전압 손실을 순차 time step 없이 계산하였다.

                        TAT 제외는 유효 route count, cycling-dependent trap density와 TAT-only 정량 비교, thermal transition을 억제한 극저온 실험·TCAD의 세 근거로 범위를 설정하였다. 이 범위에서 모델은 t_TOX=3-5 nm의 cryogenic-like TCAD를 재현하고, iterative refresh와의 차이를 장시간에서도 약 3%로 유지하면서 평균 계산 시간을 27483 s에서 3.926 s로 줄였다.
                        """
                    ),
                    "figures": [],
                },
                {
                    "title": "제 2 절 학술적 및 공학적 기여",
                    "paragraphs": paragraphs(
                        """
                        첫 번째 학술적 기여는 empirical fitting에 머물던 TBT attempt-to-escape frequency를 band-trap transition의 미시적 파라미터로 연결한 것이다. 이로써 trap energy, wavefunction overlap과 density of states가 방출률에 미치는 역할을 분리하고, oxide thickness와 cycling 변화에 대한 설명 가능성을 높였다.

                        두 번째 기여는 CTN 전하 분포의 공간 정보를 유지하면서도 3차원 TCAD보다 작은 상태 수로 문턱전압을 계산한 것이다. Cylindrical node와 determinant 관계는 균일 전하 가정을 완화하며, 다양한 초기 profile과 target time을 동일한 electrostatic matrix로 평가할 수 있게 한다.

                        세 번째 기여는 TAT 제외를 암묵적인 가정으로 두지 않고 별도의 장에서 검증한 것이다. 모델 단순화의 조건과 실패 가능성을 함께 제시하여 결과의 적용 범위를 명확히 하였으며, 향후 coupled TAT 모델로 확장할 때 필요한 상태와 파라미터를 식별하였다.

                        공학적으로는 long-term cryogenic retention의 설계 공간을 수 초 안에 탐색할 수 있는 계산 구조를 제시하였다. 계산 비용이 최대 retention time에 직접 비례하지 않으므로 구조 최적화, 공정 sensitivity, program-state 비교와 array-level 신뢰성 분석에 활용할 수 있다.
                        """
                    ),
                    "figures": [],
                },
                {
                    "title": "제 3 절 향후 연구",
                    "paragraphs": paragraphs(
                        """
                        향후 첫 번째 과제는 TOX trap 점유를 명시적으로 포함한 coupled TAT time-step-free 모델이다. CTN-to-TOX, TOX-to-channel과 recapture rate로 구성된 선형 또는 약비선형 system에 matrix exponential과 modal reduction을 적용하면 sequential time stepping을 최소화하면서 높은 cycling 조건까지 확장할 수 있다.

                        두 번째 과제는 lateral migration과 cell-to-cell coupling의 통합이다. 반경 방향 node에 word-line 방향 index를 추가하고 fringing capacitance를 포함하면 인접 셀 프로그램 패턴에 따른 retention loss를 계산할 수 있다. 이 확장은 string-level read-window와 tail distribution 예측에 필요하다.

                        세 번째 과제는 절대 극저온 파라미터의 실험적 추출이다. 여러 온도, 프로그램 레벨, dwell time과 cycling 조건에서 장시간 측정을 수행하고, trap spectroscopy와 연계하여 attempt frequency와 capture cross-section의 분포를 제한해야 한다. 이를 통해 cryogenic-like benchmark를 실제 4.2 K 수명 예측으로 발전시킬 수 있다.

                        마지막으로 제조 공정 변동과 이산 trap count를 확률 변수로 도입할 필요가 있다. 평균 profile 기반 계산을 Monte Carlo 또는 polynomial-chaos model과 결합하면 retention tail과 fail-bit probability를 빠르게 예측할 수 있다. 본 연구의 7000배 수준 계산 효율은 이러한 통계적 확장을 실용적인 시간 안에 수행할 수 있는 기반을 제공한다.
                        """
                    ),
                    "figures": [],
                },
                {
                    "title": "제 4 절 맺음말",
                    "paragraphs": paragraphs(
                        """
                        리텐션은 장시간 현상이지만 그 원인은 원자 규모 트랩의 국소 전이에서 시작된다. 따라서 신뢰성 모델은 미시적 방출 과정과 소자 전기장, 회로에서 관찰되는 문턱전압을 하나의 일관된 사슬로 연결해야 한다. 본 논문은 attempt-to-escape frequency에서 CTN 전하 node와 closed-form transient까지 이 연결을 단계적으로 구성하였다.

                        동시에 빠른 계산은 물리적 세부를 무조건 제거해서 얻어서는 안 된다. 어떤 상태를 남기고 어떤 경로를 제외했는지, 그 선택이 어느 조건에서 타당한지를 검증해야 한다. TAT 제외를 별도로 분석하고 iterative refresh로 field-feedback 오차를 확인한 것은 이러한 원칙을 반영한다.

                        제안한 time-step-free 모델은 극저온 3차원 NAND Flash의 장기 리텐션을 물리적으로 해석하면서도 설계 반복에 사용할 수 있는 계산 속도를 제공한다. 향후 TAT, lateral migration과 확률적 trap distribution이 통합되면 공정·소자·시스템 수준을 연결하는 신뢰성 예측 플랫폼으로 확장될 수 있다.
                        """
                    ),
                    "figures": [],
                },
            ],
        },
    ]
)


REFERENCES = [
    "[1] A. Goda, “Recent progress on 3D NAND flash technologies,” Electronics, vol. 10, no. 24, p. 3156, 2021, doi: 10.3390/electronics10243156.",
    "[2] E.-S. Choi and S.-K. Park, “Device considerations for high density and highly reliable 3D NAND flash cell in near future,” in Proc. IEEE IEDM, 2012, pp. 9.4.1–9.4.4, doi: 10.1109/IEDM.2012.6479011.",
    "[3] A. Refaldi et al., “Cryogenic investigation of 3-D NAND flash memory for quantum computing applications,” in Proc. IEEE IRPS, 2025, doi: 10.1109/IRPS48204.2025.10983672.",
    "[4] A. Refaldi et al., “Widely distributed time constants in the cryogenic retention of 3-D NAND flash memories,” IEEE Electron Device Lett., vol. 45, no. 10, pp. 1811–1814, 2024, doi: 10.1109/LED.2024.3435345.",
    "[5] M. Kim and H. Shin, “Analysis and compact modeling of fast detrapping in bandgap-engineered tunneling oxide of 3-D NAND flash memories,” IEEE Trans. Electron Devices, vol. 68, no. 7, pp. 3339–3345, 2021, doi: 10.1109/TED.2021.3077202.",
    "[6] M. Jin and H. Shin, “Modeling attempt-to-escape frequency for trap-to-band tunneling in bandgap-engineered tunneling oxide of 3-D NAND flash memories,” IEEE Trans. Electron Devices, 2025, doi: 10.1109/TED.2025.3589340.",
    "[7] M. Jin, H. Choi, and H. Shin, “Time-step-free physics-based modeling of retention loss in cryogenic 3-D NAND flash,” IEEE Electron Device Lett., 2026, doi: 10.1109/LED.2026.3710382.",
    "[8] S. Amoroso, A. Ghetti, A. Mauri, and A. Maconi, “A semi-analytical model for the retention time of charge-trap memories,” IEEE Trans. Electron Devices, vol. 58, no. 9, pp. 3116–3123, 2011, doi: 10.1109/TED.2011.2159010.",
    "[9] S. Kim, M. Kim, S. Choi, J. Lee, and H. Shin, “Analysis of failure mechanisms during long-term retention in charge-trap flash memories,” IEEE Trans. Electron Devices, vol. 67, no. 12, pp. 5472–5478, 2020, doi: 10.1109/TED.2020.3028349.",
    "[10] H. Jo and H. Shin, “Compact modeling of trap-assisted tunneling in the tunneling oxide of charge-trap flash memories,” IEEE Trans. Electron Devices, vol. 72, no. 4, pp. 1745–1749, 2025.",
    "[11] H. Jo, M. Kim, S. Kim, and H. Shin, “Investigation of endurance degradation in bandgap-engineered tunneling oxide for 3-D NAND flash memories,” IEEE Trans. Electron Devices, 2024, doi: 10.1109/TED.2024.3350565.",
    "[12] C. Woo, M. Kim, and H. Shin, “Modeling charge loss mechanisms in 3-D NAND flash memories,” in Proc. Symp. VLSI Technology, 2019, doi: 10.23919/VLSIT.2019.8776579.",
    "[13] C. Woo, M. Kim, and H. Shin, “A comprehensive retention model for charge-trap flash memory,” in Proc. IEEE IRPS, 2020, doi: 10.1109/IRPS45951.2020.9129306.",
    "[14] H. Choi, M. Kim, S. Kim, and H. Shin, “Effect of nitrogen content on the trap distribution and retention of silicon nitride,” IEEE Electron Device Lett., vol. 40, no. 5, pp. 702–705, 2019, doi: 10.1109/LED.2019.2905299.",
    "[15] A. Goda, “3-D NAND technology achievements and future scaling perspectives,” IEEE Trans. Electron Devices, vol. 67, no. 4, pp. 1373–1381, 2020, doi: 10.1109/TED.2020.2968079.",
    "[16] D. J. Griffiths and D. F. Schroeter, Introduction to Quantum Mechanics, 3rd ed. Cambridge, U.K.: Cambridge Univ. Press, 2018.",
    "[17] J. Wilher et al., “Over- and undercoordinated atoms as charge trapping sites in amorphous silicon nitride,” Nanomaterials, vol. 13, p. 2286, 2023, doi: 10.3390/nano13162286.",
    "[18] Y.-N. Xu and W. Y. Ching, “Electronic structure and optical properties of α and β phases of silicon nitride,” Phys. Rev. B, vol. 51, no. 24, pp. 17379–17389, 1995, doi: 10.1103/PhysRevB.51.17379.",
    "[19] J. A. López-Villanueva, P. Cartujo-Cassinello, J. Banqueri, and F. Gámiz, “Effects of direct and trap-assisted elastic tunneling on the gate current of metal-oxide-semiconductor structures,” J. Appl. Phys., vol. 91, no. 8, pp. 5116–5124, 2002, doi: 10.1063/1.1461062.",
    "[20] Synopsys, Sentaurus Device User Guide, Mountain View, CA, USA, 2022.",
    "[21] H. Choi, J. Yoo, and H. Shin, “A new physical model for program transients in charge-trap flash memory,” IEEE Trans. Electron Devices, vol. 71, no. 4, pp. 2386–2392, 2024, doi: 10.1109/TED.2024.3364587.",
    "[22] D. Verreck et al., “Understanding incremental step pulse programming in charge-trap flash memories,” in Proc. IEEE IEDM, 2021, doi: 10.1109/IEDM19574.2021.9720506.",
    "[23] I. Han and H. Shin, “Temperature dependence of lateral charge migration in 3-D NAND flash memories,” IEEE Trans. Electron Devices, vol. 73, no. 5, pp. 2747–2753, 2026, doi: 10.1109/TED.2026.3673641.",
    "[24] S. M. Sze and K. K. Ng, Physics of Semiconductor Devices, 3rd ed. Hoboken, NJ, USA: Wiley, 2007.",
    "[25] E. H. Nicollian and J. R. Brews, MOS (Metal Oxide Semiconductor) Physics and Technology. Hoboken, NJ, USA: Wiley, 1982.",
    "[26] J. G. Simmons, “Generalized formula for the electric tunnel effect between similar electrodes separated by a thin insulating film,” J. Appl. Phys., vol. 34, no. 6, pp. 1793–1803, 1963, doi: 10.1063/1.1702682.",
    "[27] R. H. Fowler and L. Nordheim, “Electron emission in intense electric fields,” Proc. R. Soc. Lond. A, vol. 119, pp. 173–181, 1928.",
    "[28] J. Frenkel, “On pre-breakdown phenomena in insulators and electronic semi-conductors,” Phys. Rev., vol. 54, pp. 647–648, 1938, doi: 10.1103/PhysRev.54.647.",
    "[29] P. A. M. Dirac, The Principles of Quantum Mechanics, 4th ed. Oxford, U.K.: Oxford Univ. Press, 1958.",
    "[30] D. K. Schroder, Semiconductor Material and Device Characterization, 3rd ed. Hoboken, NJ, USA: Wiley, 2006.",
    "[31] M. Lundstrom, Fundamentals of Carrier Transport, 2nd ed. Cambridge, U.K.: Cambridge Univ. Press, 2000.",
    "[32] C. Hu, Modern Semiconductor Devices for Integrated Circuits. Upper Saddle River, NJ, USA: Pearson, 2010.",
    "[33] Y. Taur and T. H. Ning, Fundamentals of Modern VLSI Devices, 2nd ed. Cambridge, U.K.: Cambridge Univ. Press, 2009.",
    "[34] R. Waser, Ed., Nanoelectronics and Information Technology, 3rd ed. Weinheim, Germany: Wiley-VCH, 2012.",
    "[35] IEEE, IEEE Editorial Style Manual for Authors. Piscataway, NJ, USA: IEEE, 2023.",
]

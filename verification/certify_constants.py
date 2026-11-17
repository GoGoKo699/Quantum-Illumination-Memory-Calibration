#!/usr/bin/env python3
"""Exact elementary certificate for the unknown-memory conditional receiver.

Verifies constants used in the analytic bound, without Monte Carlo or a
typical-record approximation. The optical/statistical theorem is separate.
"""
from fractions import Fraction as F
from math import factorial
import json

def exp_upper(x, degree):
    terms=[x**k/factorial(k) for k in range(degree+1)]
    first=x**(degree+1)/factorial(degree+1)
    ratio=x/F(degree+2)
    assert ratio<1
    return sum(terms)+first/(1-ratio)

def verify():
    # exp(2)>5000/677 implies 1-exp(-2)>4323/5000.
    exp2_lower=sum(F(2)**k/factorial(k) for k in range(11))
    assert exp2_lower>F(5000,677)
    u=F(4323,5000)
    # exp(5.76)<1+.95/.003, hence L*=log(1+.95/.003)>5.76.
    exp_L_upper=exp_upper(F(144,25),40)
    assert exp_L_upper<F(953,3)
    L=F(144,25)
    assert F(1311,125)**2<F(110)  # sqrt(110)>10.488
    C_inverse_lower=F(21)+2*F(1311,125)
    n=F(1,1000);B=F(10);eta_min=F(9,10);m_max=F(1,500)
    kappa_max=F(1,10)
    A_over_kappa_n=eta_min*(1+n)/(B+1+kappa_max*n)
    ratio=A_over_kappa_n*u/(1+m_max*u)*L/(L+2)*C_inverse_lower
    assert ratio>F(11,5)
    # Upperbound r<C<1e-5; total-photon cutoff tail costs >1e-4.
    A_max=eta_min*kappa_max*n*(n+1)/(B+1)
    assert A_max/(1-A_max)<F(1,100000)
    d_cutoff_lower=F(1,1000)**2/(2*F(3,1000)*F(1003,1000))
    assert d_cutoff_lower>F(1,10000)
    # Rounded return/control commands guarantee at least .99 captured power.
    capture=(F(999,1001)-F(1,1000))**2
    assert capture>F(99,100)
    assert F(99,100)*ratio>F(109,50)
    # A dyadic threshold needs neither logs nor floating-point comparison.
    assert exp_upper(F(693,1000),20)<2
    assert sum(F(694,1000)**k/factorial(k) for k in range(11))>2
    dyadic_ratio_lower=F(693,1000)*41976/13400
    assert dyadic_ratio_lower>F(217,100)
    assert F(694,1000)/13400<F(109,50)/42000
    # r < 1e-5; the norm and total-count exceptional events have larger rates.
    assert F(693,1000)-F(1,2)>F(19,100)
    assert 1-F(694,1000)>F(19,100)
    assert sum(F(3)**k/factorial(k) for k in range(11))>20
    fixed_width_ratio_lower=F(217,200)-F(3,2)*42000/2000000
    assert fixed_width_ratio_lower>F(105,100)
    result={
      'claim':'R_N <= (3/2) exp(-N*r), r > (11/5)*kappa*n*C_B',
      'N_min':20,
      'parameters':{'n':'1/1000','B':'10','eta':'[9/10,1]',
                    'nu':'[0,1/1000]','kappa':'(0,1/10]'},
      'constants':{'s':'2','u_lower':str(u),'L_lower':str(L),
                   'total_photon_cutoff':'3/1000'},
      'ratio_lower_exact':str(ratio),
      'capture_power_lower_exact':str(capture),
      'capture_099_rate_ratio_lower':str(F(99,100)*ratio),
      'dyadic_rate_ratio_lower':str(dyadic_ratio_lower),
      'finite_width_rate_ratio_lower':str(fixed_width_ratio_lower),
      'ratio_lower_decimal_for_orientation':float(ratio),
      'cutoff_tail_rate_lower':str(d_cutoff_lower),
      'method':'Exact rational Taylor bounds for exponentials; rational square check; monotone inequalities.',
      'scope':'The algebraic constant certificate depends on the separate exact conditional-count theorem; it does not certify apparatus realism or optimality.'
    }
    return result

if __name__=='__main__':
    result=verify()
    with open(__import__('pathlib').Path(__file__).with_name('conditional_memory_certificate.json'),'w') as out:
        json.dump(result,out,indent=2)
        out.write('\n')
    print(json.dumps(result,indent=2))

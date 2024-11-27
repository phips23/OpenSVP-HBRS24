<scriptConfig name="CPF_INJ" script="CPF">
  <params>
    <param name="cpf.pf_mid_inj_value" type="float">-0.95</param>
    <param name="cpf.pf_min_inj_value" type="float">-0.9</param>
    <param name="cpf.pf_mid_ab_value" type="float">0.95</param>
    <param name="cpf.pf_response_time" type="float">10.0</param>
    <param name="eut.f_min" type="float">56.0</param>
    <param name="eut.f_nom" type="float">60.0</param>
    <param name="eut.f_max" type="float">66.0</param>
    <param name="eut.v_low" type="float">116.0</param>
    <param name="eut.v_nom" type="float">120.0</param>
    <param name="eut.v_high" type="float">132.0</param>
    <param name="eut_cpf.v_in_min" type="int">300</param>
    <param name="eut.v_in_nom" type="int">400</param>
    <param name="eut_cpf.v_in_max" type="int">500</param>
    <param name="eut.p_min" type="float">1000.0</param>
    <param name="eut.var_rated" type="float">2000.0</param>
    <param name="eut.p_rated" type="float">8000.0</param>
    <param name="eut.s_rated" type="float">10000.0</param>
    <param name="cpf.pf_min_ab" type="string">Disabled</param>
    <param name="cpf.pf_mid_ab" type="string">Disabled</param>
    <param name="der.mode" type="string">Disabled</param>
    <param name="gridsim.mode" type="string">Disabled</param>
    <param name="gridsim.auto_config" type="string">Disabled</param>
    <param name="pvsim.mode" type="string">Disabled</param>
    <param name="das.mode" type="string">Disabled</param>
    <param name="hil.mode" type="string">Disabled</param>
    <param name="eut.imbalance_resp" type="string">EUT response to the average of the three-phase effective (RMS)</param>
    <param name="cpf.pf_min_inj" type="string">Enabled</param>
    <param name="cpf.pf_mid_inj" type="string">Enabled</param>
    <param name="cpf.v_in_nom" type="string">Enabled</param>
    <param name="cpf.v_in_min" type="string">Enabled</param>
    <param name="cpf.v_in_max" type="string">Enabled</param>
    <param name="eut_cpf.sink_power" type="string">No</param>
    <param name="eut.phases" type="string">Single phase</param>
    <param name="cpf.imbalance_fix" type="string">std</param>
  </params>
</scriptConfig>

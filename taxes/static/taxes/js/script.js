function taxCalculate() {
  var income = Number(document.getElementById("income").value);
  var other_income = Number(document.getElementById("other_income").value);
  const total_income = income + other_income;

  var std_deduction = Number(document.getElementById("std_deduction").value);
  var ded_80c = Number(document.getElementById("ded_80c").value);
  var pro_tax = Number(document.getElementById("pro_tax").value);
  var nps = Number(document.getElementById("nps").value);
  var hra = Number(document.getElementById("hra").value);
  var home_loan = Number(document.getElementById("home_loan").value);
  const total_deduction =
    std_deduction + ded_80c + pro_tax + nps + hra + home_loan;

  const taxable_income = total_income - total_deduction;

  const age_group_val = document.getElementById("age_group");
  const age_group = age_group_val.options[age_group_val.selectedIndex].text;

  const regime = document.getElementsByName("Regimes")[0].checked
    ? "Old Regime"
    : "New Regime";

  if (regime == "New Regime") {
    if (taxable_income <= 300000) {
      tax_on_taxable = taxable_income * 0;
    } else if (taxable_income >= 300001 && taxable_income <= 600000) {
      tax_on_taxable = (taxable_income - 300001) * 0.05;
    } else if (taxable_income >= 600001 && taxable_income <= 900000) {
      tax_on_taxable =
        (taxable_income - 600001) * 0.1 + (600000 - 300001) * 0.05;
    } else if (taxable_income >= 900001 && taxable_income <= 1200000) {
      tax_on_taxable =
        (taxable_income - 900001) * 0.15 +
        (900000 - 600001) * 0.1 +
        (600000 - 300001) * 0.05;
    } else if (taxable_income >= 1200001 && taxable_income <= 1500000) {
      tax_on_taxable =
        (taxable_income - 1200001) * 0.2 +
        (1200000 - 900001) * 0.15 +
        (900000 - 600001) * 0.1 +
        (600000 - 300001) * 0.05;
    } else {
      tax_on_taxable =
        (taxable_income - 1500001) * 0.3 +
        (1500000 - 1200001) * 0.2 +
        (1200000 - 900001) * 0.15 +
        (900000 - 600001) * 0.1 +
        (600000 - 300001) * 0.05;
    }
  } else {
    if (age_group == "Below 60") {
      if (taxable_income <= 250000) {
        tax_on_taxable = taxable_income * 0;
      } else if (taxable_income >= 250001 && taxable_income <= 500000) {
        tax_on_taxable = (taxable_income - 250001) * 0.05;
      } else if (taxable_income >= 500001 && taxable_income <= 1000000) {
        tax_on_taxable =
          (taxable_income - 500001) * 0.2 + (500000 - 250001) * 0.05;
      } else {
        tax_on_taxable =
          (taxable_income - 1000000) * 0.3 +
          (1000000 - 500001) * 0.2 +
          (500000 - 250001) * 0.05;
      }
    } else if (age_group == "60 - 80") {
      if (taxable_income <= 300000) {
        tax_on_taxable = taxable_income * 0.0;
      } else if (taxable_income >= 300001 && taxable_income <= 500000) {
        tax_on_taxable = (taxable_income - 300001) * 0.05;
      } else if (taxable_income >= 500001 && taxable_income <= 1000000) {
        tax_on_taxable =
          (taxable_income - 500001) * 0.2 + (500000 - 300001) * 0.05;
      } else {
        tax_on_taxable =
          (taxable_income - 1000001) * 0.3 +
          (1000000 - 500001) * 0.2 +
          (500000 - 300001) * 0.05;
      }
    } else {
      if (taxable_income <= 500000) {
        taxable_income = taxable_income * 0;
      } else if (taxable_income >= 500001 && taxable_income <= 1000000) {
        tax_on_taxable =
          (taxable_income - 500001) * 0.2 + (500000 - 300001) * 0.05;
      } else {
        tax_on_taxable =
          (taxable_income - 1000001) * 0.3 +
          (1000000 - 500001) * 0.2 +
          (500000 - 300001) * 0.05;
      }
    }
  }

  if (taxable_income <= 5000000) {
    surcharge = tax_on_taxable * 0;
  } else if (taxable_income >= 5000000 && taxable_income <= 10000000) {
    surcharge = tax_on_taxable * 0.1;
  } else if (taxable_income > 10000000 && taxable_income <= 20000000) {
    surcharge = tax_on_taxable * 0.15;
  } else if (taxable_income > 20000000 && taxable_income <= 50000000) {
    surcharge = tax_on_taxable * 0.25;
  } else {
    surcharge = tax_on_taxable * 0.37;
  }
  const education_cess = tax_on_taxable * 0.04;

  document.getElementById("taxable_income").value = taxable_income;
  document.getElementById("tax_on_taxable").value = Math.round(tax_on_taxable);
  document.getElementById("education_cess").value = Math.round(education_cess);
  document.getElementById("surcharge").value = Math.round(surcharge);
  document.getElementById("total_tax").value = Math.round(
    tax_on_taxable + education_cess + surcharge
  );
  document.getElementById("tax_payable").value = Math.round(
    tax_on_taxable + education_cess + surcharge
  );
}

// Copyright (C) 202" Mathieu Dutour Sikiric <mathieu.dutour@gmail.com>
// Local repo adapter binary mirroring CombinedAlgorithms.h isotropic k-space
// equivalence for use from the Python wrapper layer.
// clang-format off
#include "NumberTheoryCommon.h"
#include "NumberTheoryGmp.h"
#include "CombinedAlgorithms.h"
#include "Group.h"
#include "Permutation.h"
// clang-format on

template <typename T, typename Tint, typename Tgroup>
void process(std::string const &QFile, std::string const &Plane1File,
             std::string const &Plane2File, std::string const &choice,
             std::string const &OutFormat, std::ostream &os_out) {
  MyMatrix<T> Qmat = ReadMatrixFile<T>(QFile);
  MyMatrix<Tint> Plane1 = ReadMatrixFile<Tint>(Plane1File);
  MyMatrix<Tint> Plane2 = ReadMatrixFile<Tint>(Plane2File);
  IndefiniteCombinedAlgo<T, Tint, Tgroup> comb(std::cerr);
  auto f_get = [&]() -> std::optional<MyMatrix<Tint>> {
    if (choice == "plane") {
      return comb.INDEF_FORM_Equivalence_IsotropicKplane(
          Qmat, Qmat, Plane1, Plane2);
    }
    if (choice == "flag") {
      return comb.INDEF_FORM_Equivalence_IsotropicKflag(
          Qmat, Qmat, Plane1, Plane2);
    }
    std::cerr << "No correct choice. choice=" << choice << "\n";
    throw TerminalException{1};
  };
  std::optional<MyMatrix<Tint>> opt = f_get();
  if (OutFormat == "PYTHON") {
    if (opt) {
      WriteMatrixPYTHON(os_out, *opt);
    } else {
      os_out << "None";
    }
    os_out << "\n";
    return;
  }
  if (OutFormat == "GAP") {
    os_out << "return ";
    if (opt) {
      WriteMatrixGAP(os_out, *opt);
    } else {
      os_out << "fail";
    }
    os_out << ";\n";
    return;
  }
  std::cerr << "Failed to find a matching OutFormat\n";
  throw TerminalException{1};
}

int main(int argc, char *argv[]) {
  HumanTime time;
  try {
    if (argc != 6 && argc != 8) {
      std::cerr
          << "INDEF_FORM_TestEquivalenceIsotropicKplane [arith] [QFile] "
             "[Plane1File] [Plane2File] [choice]\n";
      std::cerr << "or\n";
      std::cerr
          << "INDEF_FORM_TestEquivalenceIsotropicKplane [arith] [QFile] "
             "[Plane1File] [Plane2File] [choice] [OutFormat] [OutFile]\n";
      throw TerminalException{1};
    }
    std::string arith = argv[1];
    std::string QFile = argv[2];
    std::string Plane1File = argv[3];
    std::string Plane2File = argv[4];
    std::string choice = argv[5];
    std::string OutFormat = "GAP";
    std::string OutFile = "stderr";
    if (argc == 8) {
      OutFormat = argv[6];
      OutFile = argv[7];
    }
    using Tidx = uint32_t;
    using Telt = permutalib::SingleSidedPerm<Tidx>;
    using TintGroup = mpz_class;
    using Tgroup = permutalib::Group<Telt, TintGroup>;
    auto f = [&](std::ostream &os) -> void {
      if (arith == "gmp") {
        using T = mpq_class;
        using Tint = mpz_class;
        return process<T, Tint, Tgroup>(QFile, Plane1File, Plane2File, choice,
                                        OutFormat, os);
      }
      std::cerr << "Failed to find matching type for arith\n";
      throw TerminalException{1};
    };
    print_stderr_stdout_file(OutFile, f);
    std::cerr << "Normal termination of "
                 "INDEF_FORM_TestEquivalenceIsotropicKplane\n";
  } catch (TerminalException const &e) {
    std::cerr << "Error in INDEF_FORM_TestEquivalenceIsotropicKplane, runtime="
              << time << "\n";
    exit(e.eVal);
  }
  runtime(time);
}

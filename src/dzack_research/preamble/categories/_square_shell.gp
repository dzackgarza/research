(form, target, reflective) -> {
  my(kept = List());
  forqfvec(v, form, target,
    if (qfeval(form, v) == target && (!reflective || content(2 * form * v) % target == 0),
      listput(kept, v);
      listput(kept, -v)
    )
  );
  Vec(kept)
}

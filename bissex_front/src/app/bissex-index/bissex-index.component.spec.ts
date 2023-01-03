import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BissexIndexComponent } from './bissex-index.component';

describe('BissexIndexComponent', () => {
  let component: BissexIndexComponent;
  let fixture: ComponentFixture<BissexIndexComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ BissexIndexComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(BissexIndexComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
